from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Shortener
from .serializer import ShortenerSerializer




class LinkShortenerViewSet(ModelViewSet):
    queryset = Shortener.objects.all()
    serializer_class = ShortenerSerializer



