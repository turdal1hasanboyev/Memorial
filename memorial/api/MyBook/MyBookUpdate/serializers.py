from rest_framework.serializers import ModelSerializer
from memorial.models import MyBook
from memorial.api.CustomUser.CustomUserLC.serializers import CustomUserLCSerializer


class MyBookUpdateSerializer(ModelSerializer):
    user = CustomUserLCSerializer(read_only=True)

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

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }