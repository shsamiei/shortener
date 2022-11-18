from .models import Shortener
from .serializers import LinkShortenerSerializer
from rest_framework.generics import ListCreateAPIView
from django.views import generic
from .services import ShortenerService


class LinkShortenerAPIView(ListCreateAPIView):
    queryset = Shortener.objects.all()
    serializer_class = LinkShortenerSerializer


class ShortenerRedirectView(generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        service = ShortenerService()
        return service.get_url(kwargs.get('shortener', ''))
        