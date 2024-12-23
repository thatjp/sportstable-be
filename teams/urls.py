from django.urls import path
from . import views

from .views import SearchResultsView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
]