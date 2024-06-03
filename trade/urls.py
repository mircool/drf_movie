from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('cards', views.CardViewSet, basename='card')


urlpatterns = [
    *router.urls,
    path('alipay/', views.AlipayApiView.as_view(), name='alipay'),
    path('callback/', views.AlipayCallbackView.as_view(), name='callback'),
]
