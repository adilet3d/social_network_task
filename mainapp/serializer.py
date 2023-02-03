from rest_framework import serializers,permissions
from mainapp.models import User,Post

class UserSerializer(serializers.Serializer):
    class Meta:
        model=User
        fields=(
            'id','name',''
        )