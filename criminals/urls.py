from django.urls import path, include
from .views import CriminalsView, CriminalDetailView

app_name = 'criminals'

urlpatterns = [
    path('', CriminalsView.as_view(), name='criminals'),
    path('search/', CriminalsView.as_view(), name='search'),
    path('details/<int:pk>', CriminalDetailView.as_view(), name='details')
]