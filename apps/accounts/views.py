from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from .models import User
from .serializers import UserSerializer
# Create your views here.

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
