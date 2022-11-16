from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Shortener
from .serializers import LinkShortenerSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response 
from rest_framework.decorators import action



class LinkShortenerAPIView(ListCreateAPIView):
    queryset = Shortener.objects.all()
    serializer_class = LinkShortenerSerializer



