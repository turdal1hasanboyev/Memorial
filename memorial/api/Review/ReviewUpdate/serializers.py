from rest_framework.serializers import ModelSerializer
from memorial.models import Book
from memorial.api.CustomUser.CustomUserLC.serializers import CustomUserLCSerializer


class BookUpdateSerializer(ModelSerializer):
    author = CustomUserLCSerializer(read_only=True)

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'sub_title',
            'slug',
            'description',
            'author',
            'published_date',
            'isbn',
            'page_count',
            'cover_image',
            'cover_video',
            'is_available',
            'language',
            'category',
            'tags',
            'awards',
            'genres',
            'views',
            'is_active',
            'created_at',
            'updated_at',
        ]

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }