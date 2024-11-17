from rest_framework.serializers import ModelSerializer
from memorial.models import Review


class ReviewDestroySerializer(ModelSerializer):    
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