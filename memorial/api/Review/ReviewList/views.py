from rest_framework.generics import ListAPIView
from memorial.models import Book
from .serializers import BookListSerializer


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('author', 'category').prefetch_related('awards', 'tags', 'genres')