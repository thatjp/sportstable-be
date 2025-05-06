from django.shortcuts import render
from datetime import date, datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import statsapi
from rest_framework.permissions import IsAuthenticated

# Create your views here.

TEAM_IDS = [
    133,
    136,
    139,
    108,
    140,
    141,
    110,
    142,
    111,
    145,
    114,
    147,
    116,
    117,
    118,
    134,
    135,
    137,
    138,
    109,
    143,
    112,
    144,
    113,
    146,
    115,
    119,
    120,
    121,
    158
]

class MLBBaseView(APIView):
    permission_classes = [IsAuthenticated]
    
    def __init__(self):
        super().__init__()


class TeamsView(MLBBaseView):
    def get(self, request):
        try:
          NL = statsapi.get('teams', params={'season': 2024, 'leagueIds': 103})
          AL = statsapi.get('teams', params={'season': 2024, 'leagueIds': 104})

          teams = NL["teams"] + AL["teams"]

          return Response(teams)
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

class TodaysScheduleView(MLBBaseView):
    def get(self, request):
        try:
            games = statsapi.schedule(date=date.today(), team="", opponent="", sportId=1, game_id=None)
            return Response(games)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LastWeekScheduleView(MLBBaseView):
    def get(self, request):
        try:
            last_week = [
                (date.today() - timedelta(days=i)).strftime('%Y-%m-%d')
                for i in range(7)
            ]

            games = []

            for day in last_week:
                daily_games = statsapi.schedule(date=day, team="", opponent="", sportId=1, game_id=None)
                games.append(daily_games)
            
            return Response(games)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)