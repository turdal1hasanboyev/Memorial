from rest_framework.serializers import ModelSerializer
from memorial.models import MyBook
from memorial.api.CustomUser.CustomUserLC.serializers import CustomUserLCSerializer
from memorial.api.Book.BookRetrieve.serializers import BookRetrieveSerializer


class MyBookRetrieveSerializer(ModelSerializer):
    user = CustomUserLCSerializer(read_only=True)
    book = BookRetrieveSerializer(read_only=True)

    class Meta:
        model = MyBook
        fields = [
            'id',
            'user',
            'book',
            'date_read',
            'is_active',
            'created_at',
            'updated_at',
        ]