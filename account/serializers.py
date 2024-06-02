from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Profile

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

    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        # 写入profile
        profile = Profile.objects.create(user=user)
        profile.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['uid', 'user', 'movies', 'avatar', 'is_upgrade', 'expire_time']


class CustomUserSerializer(UserSerializer):
    profile = ProfileSerializer(read_only=True)  # 嵌套Profile序列化器

    class Meta(UserSerializer.Meta):
        fields = (*UserSerializer.Meta.fields, 'profile')
