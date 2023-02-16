from django.shortcuts import render
from rest_framework.generics import ListAPIView
from mainapp.models import User,Post,Like,DisLikes
from mainapp.serializer import (
    UserSerializer,PostSerializer,LikeSerializer,DisLikesSerializer
)
from mainapp.mixin import LikeMixins , DisLikeMixins
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import action

# from mainapp.filters import DateLikesFilter, DateDisLikesFilter


class UserView(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
    @action(methods=['post',],detail=True,\
        serializer_class=PostSerializer, permission_classes=\
            (permissions.IsAuthenticated,))
    def add_post(self, request,*args , **kwargs):
        user=request.user
        serializer= PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data
        post=Post.objects.create(
            owner=user,
            text=data.get('text'),
            image=data.get('image'),
        )
        return Response(PostSerializer(post).data)

        


class PostView(DisLikeMixins,LikeMixins,ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
    # @action(methods=['post',],detail=True,\
    #     serializer_class=LikeSerializer, permission_classes=\
    #         (permissions.IsAuthenticated,))
    # def add_like(self, request, *args, **kwargs):
    #     user=request.user
    #     post=self.get_object()
        
    #     serializer=LikeSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     data=serializer.validated_data
    #     like= Like.objects.create(
    #         author=user,
    #         post=post
    #     )
    #     return Response(LikeSerializer(like).data)


    # @action(methods=['post',],detail=True,\
    #     serializer_class=DisLikesSerializer, permission_classes=\
    #         (permissions.IsAuthenticated,))
    # def add_dislike(self, request,*args,**kwaargs):
    #     user=request.user
    #     post=self.get_object()
        
    #     serializer=DisLikesSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     data=serializer.validated_data
    #     dislike= DisLikes.objects.create(
    #         author=user,
    #         post=post
    #     )
    #     return Response(DisLikesSerializer(dislike).data)
            



class LikesModelViewSet(ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
   
class DisLikesModelViewSet(ListAPIView):
    queryset = DisLikes.objects.all()
    serializer_class = DisLikesSerializer
  


