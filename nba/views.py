from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamdetails, leaguegamefinder
from nba_api.stats.static import teams

# Create your views here.

class NBATeamsView(APIView): 
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
          nba_teams = teams.get_teams()
          return Response(nba_teams, status=status.HTTP_200_OK)
        except Exception as e:
           return Response(status=status.HTTP_400_BAD_REQUEST)

class NBATeamView(APIView): 
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
          nba_team = teamdetails.TeamDetails(team_id=pk).get_dict()
          return Response(nba_team, status=status.HTTP_200_OK)
        except Exception as e:
           return Response(status=status.HTTP_400_BAD_REQUEST)
        
class NBAGameFinder(APIView): 
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
          game = leaguegamefinder.LeagueGameFinder(player_or_team_abbreviation='T', team_id_nullable=pk).get_dict()
          return Response(game, status=status.HTTP_200_OK)
        except Exception as e:
           return Response(status=status.HTTP_400_BAD_REQUEST)

class NBAPlayByPlay(APIView): 
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
          game = leaguegamefinder.LeagueGameFinder(player_or_team_abbreviation='T', team_id_nullable=pk).get_dict()
          return Response(game, status=status.HTTP_200_OK)
        except Exception as e:
           return Response(status=status.HTTP_400_BAD_REQUEST)

