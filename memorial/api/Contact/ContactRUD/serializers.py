from rest_framework.serializers import ModelSerializer
from memorial.models import Contact


class ContactRUDSerializer(ModelSerializer):
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
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'id': {'read_only': True},
        }