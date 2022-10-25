from django.urls import path, include
from .views import HomePage, SearchView

urlpatterns = [
    # path('', list_keys, name='list_keys'),
    path("", HomePage.as_view(), name="index"),
    path(
        "search/",
        SearchView.as_view(),
        name="search_values",
    ),
]
