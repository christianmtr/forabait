from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from food.api.serializers import SauceSerializer
from food.models import Sauce


class SauceViewSets(viewsets.ModelViewSet):
    queryset = Sauce.objects.all()
    serializer_class = SauceSerializer
    permission_classes = [IsAuthenticated]
