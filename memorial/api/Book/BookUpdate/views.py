from rest_framework.generics import UpdateAPIView
from memorial.models import Book
from .serializers import BookUpdateSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
    ]

    def get_queryset(self):
        return Book.objects.filter(is_active=True).select_related('author', 'category').prefetch_related('tags', 'awards', 'genres')
    
    def perform_update(self, serializer):
        serializer.save(author_id=self.request.user.id)