from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from .models import Like, DisLikes
from .serializer import LikeSerializer, DisLikesSerializer


class LikeMixins:
    
    @action(methods=['post'], detail=True, serializer_class=LikeSerializer)
    def add_like(self, request, *args, **kwargs):
        post = self.get_object()
        author = request.user
        like = Like.objects.filter(post=post, author=author)
        dislike = DisLikes.objects.filter(post=post, author=author)
        if like.exists():
            like.delete()
            post.like -= 1
            post.save()
            return Response({'Message': "Вы убрали лайк"}, status=status.HTTP_200_OK)
        
        else:
            if dislike.exists():
                dislike.first().delete()
                post.dislike -= 1

            Like.objects.create(author=author, post=post)
            post.like += 1
            post.save()
            return Response({"Message": "Вы поставили лайк"}, status=status.HTTP_201_CREATED)


class DisLikeMixins:
    
    @action(methods=['post'], detail=True, serializer_class=DisLikesSerializer)
    def add_dislike(self, request, *args, **kwargs):
        post = self.get_object()
        author = request.user
        like = Like.objects.filter(post=post, author=author)
        dislike = DisLikes.objects.filter(post=post, author=author)
        if dislike.exists():
            dislike.delete()
            post.dislike -= 1
            post.save()
            return Response({'Message': "Вы убрали дизлайк"}, status=status.HTTP_200_OK)
        
        else:
            if like.exists():
                like.first().delete()
                post.like -= 1

            DisLikes.objects.create(author=author, post=post)
            post.dislike += 1
            post.save()
            return Response({"Message": "Вы поставили дизлайк"}, status=status.HTTP_201_CREATED)