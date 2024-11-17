from rest_framework.generics import ListCreateAPIView
from memorial.models import Banner
from .serializers import BannerLCSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


class BannerLCAPIView(ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerLCSerializer
    permission_classes = [
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
    ]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)