from rest_framework.generics import ListAPIView
from .serializers import ReviewListSerializer
from memorial.models import Review
from rest_framework.permissions import IsAuthenticated


class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('author', 'book')