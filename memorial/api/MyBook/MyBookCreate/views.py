from rest_framework.generics import CreateAPIView
from memorial.models import MyBook
from .serializers import MyBookCreateSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MyBookCreateAPIView(CreateAPIView):
    queryset = MyBook.objects.all()
    serializer_class = MyBookCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(is_active=True).select_related('user', 'book')
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)