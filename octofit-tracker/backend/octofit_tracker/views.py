from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from pymongo import MongoClient
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from django.conf import settings

client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = list(db.users.find())
        for user in users:
            user['_id'] = str(user['_id'])
        return Response(users)
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            db.users.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamViewSet(viewsets.ViewSet):
    def list(self, request):
        teams = list(db.teams.find())
        for team in teams:
            team['_id'] = str(team['_id'])
        return Response(teams)
    def create(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            db.teams.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityViewSet(viewsets.ViewSet):
    def list(self, request):
        activities = list(db.activity.find())
        for activity in activities:
            activity['_id'] = str(activity['_id'])
        return Response(activities)
    def create(self, request):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            db.activity.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        leaderboards = list(db.leaderboard.find())
        for lb in leaderboards:
            lb['_id'] = str(lb['_id'])
        return Response(leaderboards)
    def create(self, request):
        serializer = LeaderboardSerializer(data=request.data)
        if serializer.is_valid():
            db.leaderboard.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutViewSet(viewsets.ViewSet):
    def list(self, request):
        workouts = list(db.workouts.find())
        for workout in workouts:
            workout['_id'] = str(workout['_id'])
        return Response(workouts)
    def create(self, request):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            db.workouts.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_root(request, format=None):
    # Use Codespace public URL and localhost for endpoints
    codespace_url = 'https://codespaces-674536-8000.app.github.dev'
    localhost_url = 'http://localhost:8000'
    return Response({
        'users': {
            'codespace': f'{codespace_url}/users/',
            'localhost': f'{localhost_url}/users/'
        },
        'teams': {
            'codespace': f'{codespace_url}/teams/',
            'localhost': f'{localhost_url}/teams/'
        },
        'activity': {
            'codespace': f'{codespace_url}/activity/',
            'localhost': f'{localhost_url}/activity/'
        },
        'leaderboard': {
            'codespace': f'{codespace_url}/leaderboard/',
            'localhost': f'{localhost_url}/leaderboard/'
        },
        'workouts': {
            'codespace': f'{codespace_url}/workouts/',
            'localhost': f'{localhost_url}/workouts/'
        },
    })
