from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views



urlpatterns = [

    path('', views.LinkShortenerAPIView.as_view())

]



  