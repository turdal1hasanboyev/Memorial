from rest_framework.generics import ListCreateAPIView
from memorial.models import CustomUser
from .serializers import CustomUserLCSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class CustomUserLCAPIView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserLCSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
    ]
    
    def get_queryset(self):
        return self.queryset.filter(is_active=True)