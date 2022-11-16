from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Shortener
from .serializers import LinkShortenerSerializer




class LinkShortenerViewSet(ModelViewSet):
    queryset = Shortener.objects.all()
    serializer_class = LinkShortenerSerializer