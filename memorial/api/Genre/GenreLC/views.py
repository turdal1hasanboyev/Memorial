from rest_framework.generics import ListCreateAPIView
from .serializers import GenreLCSerializer
from memorial.models import Genre


class GenreLCAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreLCSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True)