from rest_framework.generics import ListCreateAPIView
from .serializers import GenreLCSerializer
from memorial.models import Genre
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class GenreLCAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreLCSerializer
    pagination_class = None
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
    ]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)