from rest_framework import serializers                                                                                                                                                                                                                                                                                                          
from .models import Shortener
from django.conf import settings



class LinkShortenerSerializer(serializers.ModelSerializer):

    shortener_url = serializers.SerializerMethodField()

    def get_shortener_url(self, shortener: Shortener):
        return settings.MY_DOMAIN_PREFIX + shortener.shortener


    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        validated_data['shortener'] = self.context['shortener']
        return super().create(validated_data)

    class Meta:
        model = Shortener
        fields = ['url', 'shortener', 'shortener_url', 'clicks']
        read_only_fields = ['shortener', 'clicks']
