from rest_framework.generics import RetrieveUpdateDestroyAPIView
from memorial.models import Contact
from.serializers import ContactRUDSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class ContactRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactRUDSerializer
    lookup_field = 'pk'
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Contact.objects.filter(is_active=True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()