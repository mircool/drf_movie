from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from trade.models import Order


@shared_task
def add(x, y):
    return x + y


@shared_task  # 任务函数
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def batch_check_expired_orders():
    """
    批量检查过期订单
    """
    expired_orders = Order.objects.filter(pay_status='WAIT_BUYER_PAY',
                                          pay_time__lt=timezone.now() - timedelta(minutes=30))  # 30分钟未支付的订单
    for order in expired_orders:
        order.pay_status = 'TRADE_CLOSED'
        order.save()
        print(f'订单{order.order_sn}已关闭')
    return f'共关闭{expired_orders.count()}个订单'
