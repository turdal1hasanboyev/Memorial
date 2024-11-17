from rest_framework.serializers import ModelSerializer
from memorial.models import About


class AboutRUDSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = [
            'id',
            'title',
            'description',
            'image',
            'is_active',
            'created_at',
            'updated_at',
        ]

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }