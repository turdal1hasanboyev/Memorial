from rest_framework.generics import RetrieveUpdateDestroyAPIView
from memorial.models import Award
from .serializers import AwardRUDSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class AwardRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardRUDSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
    ]
    lookup_field = 'pk'

    def get_queryset(self):
        return Award.objects.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()