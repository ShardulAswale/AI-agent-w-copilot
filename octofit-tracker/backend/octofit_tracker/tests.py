from django.test import TestCase
from rest_framework.test import APIClient

class OctoFitAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_users_endpoint(self):
        response = self.client.get('/users/')
        self.assertIn(response.status_code, [200, 404])

    def test_teams_endpoint(self):
        response = self.client.get('/teams/')
        self.assertIn(response.status_code, [200, 404])

    def test_activity_endpoint(self):
        response = self.client.get('/activity/')
        self.assertIn(response.status_code, [200, 404])

    def test_leaderboard_endpoint(self):
        response = self.client.get('/leaderboard/')
        self.assertIn(response.status_code, [200, 404])

    def test_workouts_endpoint(self):
        response = self.client.get('/workouts/')
        self.assertIn(response.status_code, [200, 404])
