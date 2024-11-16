from rest_framework.generics import RetrieveUpdateDestroyAPIView
from memorial.models import Genre
from.serializers import GenreRUDSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser


class GenreRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreRUDSerializer
    lookup_field = 'pk'
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Genre.objects.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()