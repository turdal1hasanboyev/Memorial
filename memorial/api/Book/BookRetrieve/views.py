from rest_framework.generics import RetrieveAPIView
from memorial.models import Book
from .serializers import BookRetrieveSerializer


class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookRetrieveSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Book.objects.filter(is_active=True).select_related('author', 'category').prefetch_related('awards', 'tags', 'genres')