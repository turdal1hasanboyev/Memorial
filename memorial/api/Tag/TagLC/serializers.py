from rest_framework.serializers import ModelSerializer
from memorial.models import Tag


class TagLCSerializer(ModelSerializer):
    class Meta:
        model = Tag
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