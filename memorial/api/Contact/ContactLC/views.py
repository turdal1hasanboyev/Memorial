from rest_framework.generics import ListCreateAPIView
from .serializers import ContactLCSerializer
from memorial.models import Contact
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ContactLCAPIView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactLCSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)