from datetime import datetime

from django.db import transaction
from django.utils import timezone
from rest_framework import authentication, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from account.models import Profile
from config import settings
from config.permissions import IsAdminUserOrReadOnly
from trade.models import Card, Order
from trade.serializers import CardSerializer
from utils.common import get_random_code
from utils.error import Trade, response_data
from utils.zhifubao import AliPay, logger


class CardViewSet(viewsets.ModelViewSet):
    """
    会员卡管理
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    authentication_classes = [authentication.SessionAuthentication, JWTAuthentication]
    permission_classes = (IsAdminUserOrReadOnly,)


class AlipayApiView(APIView):
    """
    支付宝支付接口
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            # 防止报错，如果不存在profile则创建一个
            profile, created = Profile.objects.get_or_create(user=user)
        except Profile.DoesNotExist:
            return Response(response_data(*Trade.ProfileError), status=status.HTTP_400_BAD_REQUEST)

        card_id = request.GET.get('card_id', None)
        try:
            card = Card.objects.get(id=card_id)
        except Card.DoesNotExist:
            return Response(response_data(*Trade.CardParamError), status=status.HTTP_400_BAD_REQUEST)

        # 创建支付宝订单
        out_trade_no = 'pay' + datetime.now().strftime('%Y%m%d%H%M%S') + get_random_code(6)
        product_code = 'FAST_INSTANT_TRADE_PAY'

        try:
            Order.objects.create(
                profile=profile,
                card=card,
                order_sn=out_trade_no,
                order_mount=card.card_price,
                pay_time=timezone.now(),  # 支付时间
            )
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return Response(response_data(*Trade.OrderCreateError), status=status.HTTP_400_BAD_REQUEST)
        # 请求支付
        try:
            alipay = AliPay()
            url = alipay.trade_page(out_trade_no=out_trade_no, total_amount=str(card.card_price),
                                    subject=card.card_name,
                                    body=card.info, product_code=product_code)
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")  # 记录未预料到的错误
            return Response(response_data(*Trade.UnexpectedError), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'url': url})


class AlipayCallbackView(APIView):
    """
    支付宝支付回调接口
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        print('开始回调')
        try:
            params = request.POST.dict()
            sign = params.pop('sign')
            del params['sign_type']
            # 对字典排序
            sorted_list = sorted([(k, v) for k, v in params.items()])
            # 生成待签名字符串
            unsigned_string = '&'.join([f"{k}={v}" for k, v in sorted_list])
            # 获取签名
            alipay = AliPay()
            if not alipay.verify(unsigned_string, sign):
                return Response('fail')
            # 验证out_trade_no是否存在
            out_trade_no = params['out_trade_no']
            order = Order.objects.filter(order_sn=out_trade_no).first()
            if not order:
                return Response('fail')
            # 验证金额是否一致
            total_amount = params['total_amount']
            if total_amount != str(order.order_mount):
                return Response('fail')
            # 验证商户id是否一致
            seller_id = params['seller_id']
            if seller_id != settings.ALIPAY.get('alipay_seller_id'):
                return Response('fail')
            # 验证app_id是否一致
            app_id = params['app_id']
            if app_id != settings.ALIPAY.get('app_id'):
                return Response('fail')
            # 判断支付状态是否为TRADE_SUCCESS或TRADE_FINISHED
            trade_status = params['trade_status']  # 交易状态
            if trade_status not in ['TRADE_SUCCESS', 'TRADE_FINISHED']:
                return Response('fail')
            with transaction.atomic():
                # 更新订单状态
                order.trade_no = params['trade_no']
                order.pay_status = trade_status
                order.pay_time = params['gmt_payment']
                order.save()
                # 更新用户会员卡
                profile = order.profile
                profile.is_upgrade = True
                # 如果用户首次购买会员卡，则到期时间为当前时间加上会员卡的有效期，否则在原到期时间上加上会员卡的有效期
                if not profile.expire_time or profile.expire_time < timezone.now():
                    profile.expire_time = timezone.now() + timezone.timedelta(days=order.card.duration)
                else:
                    profile.expire_time += timezone.timedelta(days=order.card.duration)

                profile.upgrade_count += 1
                profile.save()

                return Response('success')
        except Exception as e:
            print(e)
            logger.error(f"An unexpected error occurred: {e}")
            return Response('fail')
