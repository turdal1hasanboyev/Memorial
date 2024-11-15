from rest_framework.serializers import ModelSerializer
from memorial.models import SubEmail

class SubEmailLCSerializer(ModelSerializer):
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
            'id': {"read_only": True},
            'created_at': {"read_only": True},
            'updated_at': {"read_only": True},
        }