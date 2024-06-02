from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('collects', views.CollectViewSet, basename='collect')


urlpatterns = [
    *router.urls,
]
