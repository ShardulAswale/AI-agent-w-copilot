from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate octofit_db with test data.'

    def handle(self, *args, **kwargs):
        client = MongoClient(settings.MONGO_URI)
        db = client[settings.MONGO_DB_NAME]

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Test data (example, adapt as needed)
        users = [
            {"email": "alice@example.com", "name": "Alice", "password_hash": "hash1", "team_id": "team1"},
            {"email": "bob@example.com", "name": "Bob", "password_hash": "hash2", "team_id": "team1"},
            {"email": "carol@example.com", "name": "Carol", "password_hash": "hash3", "team_id": "team2"},
        ]
        teams = [
            {"_id": "team1", "name": "Team Alpha", "members": ["alice@example.com", "bob@example.com"]},
            {"_id": "team2", "name": "Team Beta", "members": ["carol@example.com"]},
        ]
        activities = [
            {"user_id": "alice@example.com", "activity_type": "run", "duration": 30, "date": "2025-06-01"},
            {"user_id": "bob@example.com", "activity_type": "walk", "duration": 60, "date": "2025-06-01"},
            {"user_id": "carol@example.com", "activity_type": "cycle", "duration": 45, "date": "2025-06-01"},
        ]
        leaderboard = [
            {"team_id": "team1", "score": 90},
            {"team_id": "team2", "score": 45},
        ]
        workouts = [
            {"name": "Morning Run", "description": "A quick 5k run.", "suggested_by": "alice@example.com"},
            {"name": "Evening Walk", "description": "A relaxing walk.", "suggested_by": "bob@example.com"},
        ]

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activity.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated in octofit_db.'))
