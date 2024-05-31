from rest_framework import generics

from .models import Movie
from .serializers import MovieDetailSerializer, MovieListSerializer


# @api_view(['GET', 'POST'])
# def move_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieListSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = MovieListSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class MovieDetail(APIView):
#     def get(self, request, pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             raise Http404
#         serializer = MovieDetailSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             raise Http404
#         serializer = MovieDetailSerializer(movie, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             raise Http404
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
