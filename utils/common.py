# 创建随机数
import random
import string


def get_random_code(number):
    """
    生成指定长度的随机代码。

    该函数通过组合大小写字母和数字，生成指定长度的随机字符串，用于生成验证码、随机密码等。

    参数:
    number: int - 随机代码的长度。

    返回值:
    str - 生成的随机代码。
    """
    # 从大小写字母和数字中随机选择字符，生成指定长度的随机字符串
    return ''.join(random.choices(string.ascii_letters + string.digits, k=number))
