from django.urls import path
from .views import translator_view


urlpatterns = [
    path("", translator_view, name='home'),
]