from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class CustomUniqueValidator(UniqueValidator):
    def __call__(self, value, serializer_field):
        self.message = f'邮箱"{value}"已经被注册'
        super().__call__(value, serializer_field)


# 自定义用户创建序列化器
class CustomUserCreateSerializer(UserCreateSerializer):
    email = serializers.EmailField(  # 邮箱字段
        validators=[CustomUniqueValidator(queryset=User.objects.all())]  # 唯一性验证器
    )
