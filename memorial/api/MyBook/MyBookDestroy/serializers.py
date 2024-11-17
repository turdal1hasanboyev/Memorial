from rest_framework.serializers import ModelSerializer
from memorial.models import MyBook


class MyBookDestroySerializer(ModelSerializer):
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