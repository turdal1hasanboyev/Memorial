from rest_framework.generics import ListCreateAPIView
from .serializers import SubEmailLCSerializer
from memorial.models import SubEmail
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class SubEmailLCAPIView(ListCreateAPIView):
    queryset = SubEmail.objects.all()
    serializer_class = SubEmailLCSerializer
    pagination_class = None
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return SubEmail.objects.filter(is_active=True)