from django_filters import rest_framework as filters

from movie.models import Movie
from trade.models import Order


class OrderFilter(filters.FilterSet):
    """
    订单过滤器
    """

    class Meta:
        model = Order
        fields = ['order_sn', 'trade_no', 'pay_status', 'pay_type', 'order_mount', 'pay_time']


class MovieFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')  # 过滤名称

    class Meta:
        model = Movie
        fields = ['category', 'region']
