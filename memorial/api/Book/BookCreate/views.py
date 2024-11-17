from rest_framework.generics import CreateAPIView
from memorial.models import Book
from .serializers import BookCreateSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
    ]

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('author', 'category').prefetch_related('tags', 'awards', 'genres')
    
    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id)