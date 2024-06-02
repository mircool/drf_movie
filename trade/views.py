from rest_framework import authentication, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from config.permissions import IsAdminUserOrReadOnly
from trade.models import Card
from trade.serializers import CardSerializer


class CardViewSet(viewsets.ModelViewSet):
    """
    会员卡管理
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    authentication_classes = [authentication.SessionAuthentication, JWTAuthentication]
    permission_classes = (IsAdminUserOrReadOnly,)
