#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest
from django.conf import settings

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a', )
logger = logging.getLogger('')


# 读取settings.py中的配置


class AliPay:
    """
    设置配置，包括支付宝网关地址、app_id、应用私钥、支付宝公钥等，其他配置值可以查看AlipayClientConfig的定义。
    """
    alipay_client_config = AlipayClientConfig() # 实例化一个配置对象
    alipay_client_config.server_url = settings.ALIPAY.get('server_url') # 支付宝网关地址
    alipay_client_config.app_id = settings.ALIPAY.get('app_id') # app_id
    alipay_client_config.app_private_key = settings.ALIPAY.get('app_private_key')   # 应用私钥
    alipay_client_config.alipay_public_key = settings.ALIPAY.get('alipay_public_key')   # 支付宝公钥

    def __init__(self):
        """
        得到客户端对象。
        注意，一个alipay_client_config对象对应一个DefaultAlipayClient，定义DefaultAlipayClient对象后，alipay_client_config不得修改，如果想使用不同的配置，请定义不同的DefaultAlipayClient。
        logger参数用于打印日志，不传则不打印，建议传递。
        """
        self.client = DefaultAlipayClient(alipay_client_config=self.alipay_client_config, logger=logger)

    def trade_page(self, out_trade_no, total_amount, subject, body, product_code):
        """
        页面接口示例：alipay.trade.page.pay
        """
        # 对照接口文档，构造请求对象
        model = AlipayTradePagePayModel()  # 实例化一个请求对象
        model.out_trade_no = out_trade_no  # 商户订单号
        model.total_amount = total_amount  # 金额
        model.subject = subject  # 订单标题
        model.body = body  # 订单描述
        model.product_code = product_code  # 销售产品码
        request = AlipayTradePagePayRequest(biz_model=model)
        # 得到构造的请求，如果http_method是GET，则是一个带完成请求参数的url，如果http_method是POST，则是一段HTML表单片段
        response = self.client.page_execute(request, http_method="GET")
        return response
