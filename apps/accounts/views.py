from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import User
from .serializers import UserSerializer
# Create your views here.

class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
