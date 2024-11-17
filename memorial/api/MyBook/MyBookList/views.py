from rest_framework.generics import ListAPIView
from memorial.models import MyBook
from .serializers import MyBookListSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MyBookListAPIView(ListAPIView):
    queryset = MyBook.objects.all()
    serializer_class = MyBookListSerializer
    pagination_class = None
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'book')