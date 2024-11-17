from rest_framework.serializers import ModelSerializer
from memorial.models import Book


class BookDestroySerializer(ModelSerializer):
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