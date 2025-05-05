from django.urls import path
from .views import TeamsView, TeamView, PlayersView, PlayerView, GamesView, GameView

urlpatterns = [
    path('teams/', TeamsView.as_view(), name='teams'),
    path('teams/<int:team_id>/', TeamView.as_view(), name='team'),
    path('players/', PlayersView.as_view(), name='players'),
    path('players/<int:player_id>/', PlayerView.as_view(), name='player'),
    path('games/', GamesView.as_view(), name='games'),
    path('games/<int:game_id>/', GameView.as_view(), name='game'),
] 