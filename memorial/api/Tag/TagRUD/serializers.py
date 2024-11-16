from rest_framework.serializers import ModelSerializer
from memorial.models import Tag


class TagRUDSerializer(ModelSerializer):
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
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'id': {'read_only': True},
        }