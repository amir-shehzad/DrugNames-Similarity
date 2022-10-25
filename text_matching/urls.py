from django.urls import path, include
from .views import list_keys, search_similar_values

urlpatterns = [
    path('', list_keys, name='list_keys'),
    path('search/', search_similar_values, name='search_values'),    
]