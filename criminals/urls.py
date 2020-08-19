from django.urls import path, include
from . import views

app_name = 'criminals'

urlpatterns = [
    path('', views.display, name='criminals'),
    path('search/', views.search, name='search'),
]