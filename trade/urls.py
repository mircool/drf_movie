from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('cards', views.CardViewSet, basename='card')


urlpatterns = [
    *router.urls,
]
