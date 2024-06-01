from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('movies', views.MovieViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = [
    *router.urls,
]
