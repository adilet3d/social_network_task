from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from mainapp.models import User,Post
from mainapp.serializer import (
    UserSerializer,PostSerializer,AuthorizationSerializer,\
        RegistrationSerializer
)
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.decorators import action



class UserView(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
    @action(methods=['post',],detail=True,\
        serializer_class=PostSerializer, permission_classes=\
            (permissions.IsAuthenticatedOrReadOnly))
    def add_post(self, request,*args , **kwargs):
        user=self.get_object()
        serializer= PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data
        post=Post.objects.create(
            user=user,
            text=data.get('text'),
            image=data.get('image'),
            create_at=data.get('create_at'),
        )
        return Response(PostSerializer(post).data)

        


class PostView(ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    



class RegistrationView(APIView):
    def post(self,request):
        serializer= RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data


        username= data.get('username')
        email=data.get('email')
        password=data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({'message':'User with such name is already exists'})
        user= User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        token=Token.objects.create(user=user)
        return Response({'token':token.key})

class AuthorizationView(APIView):
    def post(self, requset):
        serializer=AuthorizationSerializer
        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data
        
        
        username=data.get('username')
        password=data.get('password')
        user= User.objects.filter(username=username).first()
        
        if user is not None:
            if check_password(password, user.password):
                token,_=Token.objects.get_or_create(user=user)
                return Response({'token:':token.key})
            return Response ({'error':'Password is not valid'}, status=400)
        return Response({'error':'This username is not registred'},status=400)

