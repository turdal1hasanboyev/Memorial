from rest_framework.generics import RetrieveUpdateDestroyAPIView
from memorial.models import Tag
from .serializers import TagRUDSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser


class TagRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagRUDSerializer
    lookup_field = 'pk'
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthenticated,
        IsAdminUser,
    ]

    def get_queryset(self):
        return Tag.objects.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()