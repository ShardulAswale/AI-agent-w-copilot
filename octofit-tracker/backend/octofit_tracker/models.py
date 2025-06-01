# MongoDB models for OctoFit collections (users, teams, activity, leaderboard, workouts)
# These are not Django ORM models, but plain Python classes for MongoDB documents

class User:
    def __init__(self, email, name, password_hash, team_id=None, _id=None):
        self._id = _id
        self.email = email
        self.name = name
        self.password_hash = password_hash
        self.team_id = team_id

class Team:
    def __init__(self, name, members=None, _id=None):
        self._id = _id
        self.name = name
        self.members = members or []

class Activity:
    def __init__(self, user_id, activity_type, duration, date, _id=None):
        self._id = _id
        self.user_id = user_id
        self.activity_type = activity_type
        self.duration = duration
        self.date = date

class Leaderboard:
    def __init__(self, team_id, score, _id=None):
        self._id = _id
        self.team_id = team_id
        self.score = score

class Workout:
    def __init__(self, name, description, suggested_by, _id=None):
        self._id = _id
        self.name = name
        self.description = description
        self.suggested_by = suggested_by
