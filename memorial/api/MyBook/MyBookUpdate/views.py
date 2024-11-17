from rest_framework.generics import UpdateAPIView
from memorial.models import MyBook
from .serializers import MyBookUpdateSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MyBookUpdateAPIView(UpdateAPIView):
    queryset = MyBook.objects.all()
    serializer_class = MyBookUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return MyBook.objects.filter(is_active=True).select_related('user', 'book')
    
    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user.id)