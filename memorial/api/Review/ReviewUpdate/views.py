from rest_framework.generics import UpdateAPIView
from .serializers import ReviewUpdateSerializer
from memorial.models import Review
from rest_framework.permissions import IsAuthenticated


class ReviewUpdateAPIView(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('author', 'book')
    
    def perform_update(self, serializer):
        serializer.save(author_id=self.request.user.id)