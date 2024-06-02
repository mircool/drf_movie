from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from movie.serializers import MovieSerializer
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
    # 显示收藏的电影对象，id 和 name 字段
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['uid', 'user', 'movies']
