from rest_framework.generics import RetrieveAPIView
from .serializers import ReviewRetrieveSerializer
from memorial.models import Review
from rest_framework.permissions import IsAuthenticated


class ReviewRetrieveAPIView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewRetrieveSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Review.objects.filter(is_active=True).select_related('author', 'book')