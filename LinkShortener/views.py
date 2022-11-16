from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Shortener


class LinkShortenerViewSet(ModelViewSet):
    queryset = Shortener.objects.all()
    







