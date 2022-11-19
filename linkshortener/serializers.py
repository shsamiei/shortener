from rest_framework import serializers                                                                                                                                                                                                                                                                                                          
from .models import Shortener
from .services import ShortenerService

MY_DOMAIN_PREFIX = 'http://127.0.0.1:8000/'

class LinkShortenerSerializer(serializers.ModelSerializer):

    shortener = serializers.CharField(max_length=255, read_only=True)
    clicks = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        url = validated_data['url']
        new_link = ShortenerService()
        shortener = MY_DOMAIN_PREFIX + new_link.long_to_short_url(url)
        return Shortener.objects.create(url=url, shortener=shortener)

        
    class Meta:
        model = Shortener
        fields = ['url', 'shortener', 'clicks']