from rest_framework.serializers import ModelSerializer
from memorial.models import Review
from memorial.api.CustomUser.CustomUserLC.serializers import CustomUserLCSerializer
from memorial.api.Book.BookRetrieve.serializers import BookRetrieveSerializer


class ReviewRetrieveSerializer(ModelSerializer):
    author = CustomUserLCSerializer(read_only=True)
    book = BookRetrieveSerializer(read_only=True)
    
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