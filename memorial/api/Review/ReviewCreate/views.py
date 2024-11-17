from rest_framework.generics import CreateAPIView
from .serializers import ReviewCreateSerializer
from memorial.models import Review
from rest_framework.permissions import IsAuthenticated


class ReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(is_active=True).select_related('author', 'book')
    
    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.id)