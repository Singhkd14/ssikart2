from django.urls import path, include
from home.views import *





urlpatterns = [
    path("", sec, name="ssi-home"),
    path("about", about, name="ssi-about")
]
