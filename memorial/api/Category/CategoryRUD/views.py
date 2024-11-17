from rest_framework.generics import RetrieveUpdateDestroyAPIView
from memorial.models import Category
from .serializers import CategoryRUDSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class CategoryRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRUDSerializer
    lookup_field = 'slug'
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
    ]

    def get_queryset(self):
        return Category.objects.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()