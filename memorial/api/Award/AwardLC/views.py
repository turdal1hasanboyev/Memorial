from rest_framework.generics import ListCreateAPIView
from memorial.models import Award
from .serializers import AwardLCSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class AwardLCAPIView(ListCreateAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardLCSerializer
    pagination_class = None
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAdminUser,
    ]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)