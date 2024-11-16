from rest_framework.serializers import ModelSerializer
from memorial.models import CustomUser


class CustomUserRUDSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'description',
            'note',
            'gender',
            'phone_number',
            'birthday',
            'adress',
            'image',
            'video',
            'is_superuser',
            'date_joined',
            'last_login',
            'is_staff',
            'is_active',
            'created_at',
            'updated_at',
            ]
        
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'date_joined': {'read_only': True},
            'last_login': {'read_only': True},
        }