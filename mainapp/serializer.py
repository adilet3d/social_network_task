from rest_framework import serializers,exceptions
from mainapp.models import User,Post

class UserSerializer(serializers.Serializer):
    class Meta:
        model=User
        fields=(
            'id','name','second_name','date_of_birth','country',
        )

class PostSerializer(serializers.Serializer):
    user= UserSerializer
    class Meta:
        model=Post
        fields=(
            'id','text','image','create_at','user',
        )
        


class RegistrationSerializer(serializers.Serializer):
    username= serializers.CharField()
    password= serializers.CharField()
    email= serializers.CharField()
    def validate_password(self,value):
        if len(value) <8:
            raise exceptions.ValidationError('Password is too short')
        elif len (value) >24:
            raise exceptions.ValidationError ('Password is too long')
        return value


class AuthorizationSerializer(serializers.Serializer):
    username= serializers.CharField()
    password= serializers.CharField()