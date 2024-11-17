from rest_framework.generics import RetrieveUpdateDestroyAPIView
from memorial.models import Banner
from .serializers import BannerRUDSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


class BannerRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerRUDSerializer
    permission_classes = [
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
    ]
    lookup_field = 'pk'

    def get_queryset(self):
        return Banner.objects.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()