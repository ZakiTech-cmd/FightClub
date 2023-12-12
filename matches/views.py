from rest_framework.viewsets import ModelViewSet

from utils.permissions import IsAdminOrReadOnly
from .models import Match
from .serializers import MatchSerializer


# Create your views here.
class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAdminOrReadOnly]
