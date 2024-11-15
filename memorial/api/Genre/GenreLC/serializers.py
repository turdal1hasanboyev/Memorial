from rest_framework.serializers import ModelSerializer
from memorial.models import Genre


class GenreLCSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = [
            'id',
            'name',
            'is_active',
            'created_at',
            'updated_at',
        ]

        extra_kwargs = {
            'id': {"read_only": True},
            'created_at': {"read_only": True},
            'updated_at': {"read_only": True},
        }