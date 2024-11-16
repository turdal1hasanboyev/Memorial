from rest_framework.generics import ListCreateAPIView
from memorial.models import CustomUser
from .serializers import CustomUserLCSerializer


class CustomUserLCAPIView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserLCSerializer
    
    def get_queryset(self):
        return self.queryset.filter(is_active=True)