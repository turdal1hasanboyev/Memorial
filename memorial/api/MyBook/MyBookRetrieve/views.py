from rest_framework.generics import RetrieveAPIView
from memorial.models import MyBook
from .serializers import MyBookRetrieveSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MyBookRetrieveAPIView(RetrieveAPIView):
    queryset = MyBook.objects.all()
    serializer_class = MyBookRetrieveSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return MyBook.objects.filter(is_active=True).select_related('user', 'book')