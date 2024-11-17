from rest_framework.serializers import ModelSerializer
from memorial.models import Book
from memorial.api.CustomUser.CustomUserLC.serializers import CustomUserLCSerializer
from memorial.api.Category.CategoryLC.serializers import CategoryLCSerializer
from memorial.api.Tag.TagLC.serializers import TagLCSerializer
from memorial.api.Award.AwardLC.serializers import AwardLCSerializer
from memorial.api.Genre.GenreLC.serializers import GenreLCSerializer


class BookListSerializer(ModelSerializer):
    author = CustomUserLCSerializer(read_only=True)
    category = CategoryLCSerializer(read_only=True)
    tags = TagLCSerializer(many=True, read_only=True)
    awards = AwardLCSerializer(many=True, read_only=True)
    genres = GenreLCSerializer(many=True, read_only=True)

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