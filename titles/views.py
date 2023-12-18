from rest_framework.viewsets import ModelViewSet

from titles.models import Title
from titles.serializers import TitleSerializer
from utils.permissions import IsAdminOrReadOnly


class TitleViewSet(ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAdminOrReadOnly]

