from rest_framework.serializers import ModelSerializer
from memorial.models import Contact


class ContactLCSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'name',
            'email',
            'phone_number',
            'subject',
            'message',
            'is_active',
            'created_at',
            'updated_at',
        ]

        extra_kwargs = {
            'id': {"read_only": True},
            'created_at': {"read_only": True},
            'updated_at': {"read_only": True},
        }