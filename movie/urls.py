from django.urls import path

from . import views

urlpatterns = [
    path('', views.move_list, name='movie_list'),
]
