from .models import Shortener
from .serializers import LinkShortenerSerializer
from rest_framework.generics import ListCreateAPIView
from django.views import generic
from .services import ShortenerService


class LinkShortenerAPIView(ListCreateAPIView):
    queryset = Shortener.objects.all()
    serializer_class = LinkShortenerSerializer
    

    def get_serializer_context(self):
        service = ShortenerService()

        if self.request.POST.get('url'):
            shortener = service.long_to_short_url(self.request.POST.get('url'))
            return {'shortener':shortener}

    def perform_create(self, serializer):
        if Shortener.objects.filter(url=serializer.validated_data['url']).exists():
            return 
        return super().perform_create(serializer)



class ShortenerRedirectView(generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        service = ShortenerService()
        return service.get_long_url(kwargs.get('shortener', ''))
