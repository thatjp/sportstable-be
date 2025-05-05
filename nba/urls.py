from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_teams_list, name='nba_teams'),
    path('<int:pk>/', views.NBATeamView.as_view(), name='nba_team'),
    path('games/<int:pk>/', views.NBAGameFinder.as_view(), name='nba_team_game'),
]