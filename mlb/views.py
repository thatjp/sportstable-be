from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import statsapi
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class MLBBaseView(APIView):
    permission_classes = [IsAuthenticated]
    
    def __init__(self):
        super().__init__()


class TeamsView(MLBBaseView):
    def get(self, request):
        try:
          
          return Response(statsapi.get('teams', params={'season': 2024, 'leagueIds': 103}))
            # teams = self.mlb_api.teams()
            # return Response(teams)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TeamView(MLBBaseView):
    def get(self, request, team_id):
        try:
            team = self.mlb_api.team(team_id)
            return Response(team)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PlayersView(MLBBaseView):
    def get(self, request):
        try:
            players = self.mlb_api.players()
            return Response(players)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PlayerView(MLBBaseView):
    def get(self, request, player_id):
        try:
            player = self.mlb_api.player(player_id)
            return Response(player)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GamesView(MLBBaseView):
    def get(self, request):
        try:
            date = request.query_params.get('date')
            if date:
                games = self.mlb_api.games(date=date)
            else:
                games = self.mlb_api.games()
            return Response(games)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GameView(MLBBaseView):
    def get(self, request, game_id):
        try:
            game = self.mlb_api.game(game_id)
            return Response(game)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
