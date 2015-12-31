from core.serializers import FighterSerializer
from core.models import Fighter
from rest_framework import viewsets


class FighterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer
