from rest_framework.generics import ListCreateAPIView
from .serializers import TagLCSerializer
from memorial.models import Tag
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class TagLCAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagLCSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
        ]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)