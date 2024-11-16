from rest_framework.generics import RetrieveUpdateDestroyAPIView
from memorial.models import CustomUser
from .serializers import CustomUserRUDSerializer


class CustomUserRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRUDSerializer
    lookup_field = 'pk'
    
    def get_queryset(self):
        return CustomUser.objects.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()