from django.urls import path
from .views import endpoint_view 

urlpatterns = [
    path('api/translate/', endpoint_view, name='api'),
]