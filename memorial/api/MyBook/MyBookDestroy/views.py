from rest_framework.generics import DestroyAPIView
from memorial.models import MyBook
from .serializers import MyBookDestroySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MyBookDestroyAPIView(DestroyAPIView):
    queryset = MyBook.objects.all()
    serializer_class = MyBookDestroySerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return MyBook.objects.filter(is_active=True).select_related('user', 'book')
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()