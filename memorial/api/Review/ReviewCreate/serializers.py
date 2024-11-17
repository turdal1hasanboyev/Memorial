from rest_framework.serializers import ModelSerializer
from memorial.models import Review
from memorial.api.CustomUser.CustomUserLC.serializers import CustomUserLCSerializer


class ReviewCreateSerializer(ModelSerializer):
    author = CustomUserLCSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = [
            'id',
            'author',
            'book',
            'rate',
            'review',
            'bookshelve',
            'date_started',
            'date_ended',
            'is_active',
            'created_at',
            'updated_at',
        ]

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }