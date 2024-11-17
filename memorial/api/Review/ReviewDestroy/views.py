from rest_framework.generics import DestroyAPIView
from memorial.models import Book
from .serializers import BookDestroySerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class BookDestroyAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDestroySerializer
    lookup_field = 'slug'
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
    ]

    def get_queryset(self):
        return Book.objects.filter(is_active=True).select_related('author', 'category').prefetch_related('awards', 'tags', 'genres')
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()