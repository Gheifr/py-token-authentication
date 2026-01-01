from django.contrib.auth import get_user_model
from rest_framework import generics

from user.serializers import UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CreateUser(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
