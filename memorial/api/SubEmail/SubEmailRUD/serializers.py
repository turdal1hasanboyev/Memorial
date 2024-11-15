from rest_framework.serializers import ModelSerializer
from memorial.models import SubEmail


class SubEmailRUDSerializer(ModelSerializer):
    class Meta:
        model = SubEmail
        fields = [
            'id',
            'email',
            'is_active',
            'created_at',
            'updated_at',
        ]

        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'id': {'read_only': True},
        }