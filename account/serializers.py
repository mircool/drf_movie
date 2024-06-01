from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


# 自定义用户创建序列化器
class CustomUserCreateSerializer(UserCreateSerializer):
    email = serializers.EmailField(  # 邮箱字段
        validators=[UniqueValidator(queryset=User.objects.all())]  # 唯一性验证器
    )
