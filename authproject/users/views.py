from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
