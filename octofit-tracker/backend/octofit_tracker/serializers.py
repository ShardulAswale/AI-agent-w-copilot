from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    password_hash = serializers.CharField(max_length=128)
    team_id = serializers.CharField(max_length=24, required=False, allow_null=True)
    _id = serializers.CharField(max_length=24, required=False)

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.CharField(max_length=24), required=False)
    _id = serializers.CharField(max_length=24, required=False)

class ActivitySerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=24)
    activity_type = serializers.CharField(max_length=50)
    duration = serializers.IntegerField()
    date = serializers.DateField()
    _id = serializers.CharField(max_length=24, required=False)

class LeaderboardSerializer(serializers.Serializer):
    team_id = serializers.CharField(max_length=24)
    score = serializers.IntegerField()
    _id = serializers.CharField(max_length=24, required=False)

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    suggested_by = serializers.CharField(max_length=24)
    _id = serializers.CharField(max_length=24, required=False)
