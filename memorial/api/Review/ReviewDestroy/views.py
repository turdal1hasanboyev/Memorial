from rest_framework.generics import DestroyAPIView
from .serializers import ReviewDestroySerializer
from memorial.models import Review
from rest_framework.permissions import IsAuthenticated


class ReviewDestroyAPIView(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDestroySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('author', 'book')
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()