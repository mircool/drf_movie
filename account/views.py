from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from movie.models import Movie
from movie.serializers import MovieSerializer
from .models import Profile
from .serializers import ProfileSerializer


# Create your views here.
class CollectViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        profile, _ = Profile.objects.get_or_create(user=user)  # 使用 get_or_create 以防 Profile 不存在

        # 验证 movie_id 是否在请求数据中且为有效整数
        if 'movie_id' not in request.data:
            raise ValidationError({'movie_id': '电影ID是必须的。'})

        try:
            movie_id = int(request.data['movie_id'])
        except ValueError:
            raise ValidationError({'movie_id': '电影ID必须是整数。'})

        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise Http404("电影不存在")

        # 此处假设 profile.movies 是一个多对多关系
        profile.movies.add(movie)

        # 可以使用序列化器来序列化创建后的 profile 对象
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
