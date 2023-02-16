from rest_framework import serializers,exceptions
from mainapp.models import User,Post,Like,DisLikes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=(
            'id','username','password',
            )


class PostSerializer(serializers.ModelSerializer):
    # user= UserSerializer()
    class Meta:
        model=Post
        fields=(
            'id','owner','text','image','create_at','like','dislike',
        )
        
class LikeSerializer(serializers.ModelSerializer):

    post = serializers.ReadOnlyField(source='post.title')
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:

        model = Like
        fields = ['id', 'post', 'author', 'created_at', ]
        read_only_fields = ['created_at', ]


class DisLikesSerializer(serializers.ModelSerializer):
    
    post = serializers.ReadOnlyField(source='post.title')
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:

        model = DisLikes
        fields = ['id', 'post', 'author', 'created_at', ]
        read_only_fields = ['created_at', ]
