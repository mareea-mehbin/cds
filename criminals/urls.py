from django.urls import path, include
from .views import CriminalsView

app_name = 'criminals'

urlpatterns = [
    path('', CriminalsView.as_view(), name='criminals'),
    path('search/', CriminalsView.as_view(), name='search'),
]