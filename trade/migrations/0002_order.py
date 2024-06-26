# Generated by Django 5.0.6 on 2024-06-02 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_created_at_profile_updated_at'),
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_sn', models.CharField(help_text='订单号', max_length=30, unique=True, verbose_name='订单号')),
                ('trade_no', models.CharField(blank=True, help_text='交易号', max_length=100, null=True, unique=True, verbose_name='交易号')),
                ('pay_status', models.CharField(choices=[('TRADE_SUCCESS', '交易成功'), ('TRADE_CLOSED', '交易关闭'), ('WAIT_BUYER_PAY', '等待买家付款'), ('TRADE_FINISHED', '交易结束'), ('TRADE_FAIL', '交易失败'), ('PAYING', '支付中')], default='WAIT_BUYER_PAY', help_text='支付状态', max_length=20, verbose_name='支付状态')),
                ('pay_type', models.CharField(choices=[('ALIPAY', '支付宝'), ('WECHAT', '微信'), ('UNIONPAY', '银联')], help_text='支付类型', max_length=20, verbose_name='支付类型')),
                ('order_mount', models.DecimalField(decimal_places=2, help_text='订单金额', max_digits=10, verbose_name='订单金额')),
                ('pay_time', models.DateTimeField(blank=True, help_text='支付时间', null=True, verbose_name='支付时间')),
                ('card', models.ForeignKey(help_text='会员卡', on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='trade.card', verbose_name='会员卡')),
                ('profile', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to='account.profile', verbose_name='用户')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
    ]
