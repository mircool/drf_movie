from django.contrib import admin

from .models import Card, Order


class CardAdmin(admin.ModelAdmin):
    list_display = ['card_name', 'card_price', 'duration']
    search_fields = ['card_name']
    list_filter = ['card_name', 'card_price', 'duration']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['profile', 'card', 'order_sn', 'trade_no', 'pay_status', 'pay_type', 'order_mount', 'pay_time']
    search_fields = ['profile', 'card', 'order_sn', 'trade_no', 'pay_status', 'pay_type', 'order_mount', 'pay_time']
    list_filter = ['profile', 'card', 'order_sn', 'trade_no', 'pay_status', 'pay_type', 'order_mount', 'pay_time']


admin.site.register(Order, OrderAdmin)
admin.site.register(Card, CardAdmin)
