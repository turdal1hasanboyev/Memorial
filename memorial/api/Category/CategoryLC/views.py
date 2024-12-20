from rest_framework.generics import ListCreateAPIView
from .serializers import CategoryLCSerializer
from memorial.models import Category
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class CategoryLCAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryLCSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
        ]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)