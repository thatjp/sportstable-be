from rest_framework import generics
from django.views.generic import ListView

from .serializers import TeamSerializer
from .models import Team

# Create your views here.


class SearchResultsView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer