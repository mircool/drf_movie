from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from movie.models import Movie
from movie.serializers import MovieSerializer
from .models import Profile


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
            raise ValidationError({'message': '电影ID是必须的'})

        try:
            movie_id = int(request.data['movie_id'])
        except ValueError:
            raise ValidationError({'message': '电影ID必须是整数'})

        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise Http404("电影不存在")

        # 此处假设 profile.movies 是一个多对多关系
        profile.movies.add(movie)

        return Response({'movie_id': movie_id}, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        # 取消收藏
        user = request.user
        profile, _ = Profile.objects.get_or_create(user=user)

        # 从path参数中获取电影ID
        movie_id = kwargs.get('pk')
        try:
            movie_id = int(movie_id)
        except ValueError:
            raise ValidationError({'message': '电影ID必须是整数'})

        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise Http404("电影不存在")

        # 判断是否收藏了该电影
        if movie not in profile.movies.all():
            raise ValidationError({'message': '未收藏该电影'})

        profile.movies.remove(movie)

        return Response({'message': '取消收藏成功'})

    def list(self, request, *args, **kwargs):
        user = request.user
        profile, _ = Profile.objects.get_or_create(user=user)

        movies = profile.movies.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def is_collected(self, request, pk=None):
        user = request.user
        profile, _ = Profile.objects.get_or_create(user=user)

        try:
            movie_id = int(pk)
        except ValueError:
            raise ValidationError({'message': '电影ID必须是整数'})

        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise Http404("电影不存在")

        is_collected = movie in profile.movies.all()

        return Response({'is_collected': is_collected})
