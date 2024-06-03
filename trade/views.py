from datetime import datetime

from django.utils import timezone
from rest_framework import authentication, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from account.models import Profile
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
