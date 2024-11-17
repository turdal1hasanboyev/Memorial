from rest_framework.generics import ListCreateAPIView
from memorial.models import About
from .serializers import AboutLCSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


class AboutLCAPIView(ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutLCSerializer
    permission_classes = [
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
    ]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)