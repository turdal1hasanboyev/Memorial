from rest_framework.serializers import ModelSerializer
from memorial.models import Banner


class BannerLCSerializer(ModelSerializer):
    class Meta:
        model = Banner
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