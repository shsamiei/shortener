from rest_framework import serializers                                                                                                                                                                                                                                                                                                          
from .models import Shortener



class LinkShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ['url', 'shortener']

