from django.db import models

from config.models import BaseModel


class Card(BaseModel):
    card_name = models.CharField(max_length=100, unique=True, verbose_name='会员卡名称', help_text='会员卡名称')
    card_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='会员卡价格', help_text='会员卡价格')
    duration = models.IntegerField(verbose_name='有效期', help_text='有效期')
    info = models.TextField(verbose_name='会员卡说明', help_text='会员卡说明')

    class Meta:
        verbose_name = '会员卡'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.card_name


class Order(BaseModel):
    ORDER_STATUS = (
        ('TRADE_SUCCESS', '交易成功'),
        ('TRADE_CLOSED', '交易关闭'),
        ('WAIT_BUYER_PAY', '等待买家付款'),
        ('TRADE_FINISHED', '交易结束'),
        ('TRADE_FAIL', '交易失败'),
        ('PAYING', '支付中'),
    )

    PAY_TYPE = (
        ('ALIPAY', '支付宝'),
        ('WECHAT', '微信'),
        ('UNIONPAY', '银联'),
    )

    profile = models.ForeignKey('account.Profile', on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    card = models.ForeignKey(Card, on_delete=models.DO_NOTHING, related_name='+', verbose_name='会员卡',
                             help_text='会员卡')
    order_sn = models.CharField(max_length=30, unique=True, verbose_name='订单号', help_text='订单号')
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name='交易号',
                                help_text='交易号')
    pay_status = models.CharField(max_length=20, choices=ORDER_STATUS, default='WAIT_BUYER_PAY',
                                  verbose_name='支付状态',
                                  help_text='支付状态')
    pay_type = models.CharField(max_length=20, choices=PAY_TYPE, default='ALIPAY', verbose_name='支付类型',
                                help_text='支付类型')
    order_mount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='订单金额', help_text='订单金额')
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name='支付时间', help_text='支付时间')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_sn
