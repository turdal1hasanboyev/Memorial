from rest_framework.generics import RetrieveUpdateDestroyAPIView
from memorial.models import SubEmail
from .serializers import SubEmailRUDSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class SubEmailRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SubEmail.objects.all()
    serializer_class = SubEmailRUDSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return SubEmail.objects.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()