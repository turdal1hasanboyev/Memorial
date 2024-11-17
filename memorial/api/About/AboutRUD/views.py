from rest_framework.generics import RetrieveUpdateDestroyAPIView
from memorial.models import About
from .serializers import AboutRUDSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


class AboutRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutRUDSerializer
    permission_classes = [
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
    ]
    lookup_field = 'pk'

    def get_queryset(self):
        return About.objects.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()