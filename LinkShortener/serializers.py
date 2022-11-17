from rest_framework import serializers                                                                                                                                                                                                                                                                                                          
from .models import Shortener
from .services import ShortenerService

class LinkShortenerSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        url = validated_data['url']
        new_link = ShortenerService()
        shortener = new_link.long_to_short_url(url)
        return Shortener.objects.create(url=url, shortener=shortener)

        
    class Meta:
        model = Shortener
        fields = ['url', 'shortener']

