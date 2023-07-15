from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK
# Create your tests here.

class HackathonListDataTestCase(APITestCase):
    def test_hackathon_list(self):
        url = '/api/v1/get-hackathon-list/'
        response=self.client.get(url)
        self.assertEqual(response.status_code,HTTP_200_OK)
    
    def test_live_hackathon_list(self):
        url = '/api/v1/get-hackathon-list/live/'
        response=self.client.get(url)
        self.assertEqual(response.status_code,HTTP_200_OK)
    
    def test_past_hackathon_list(self):
        url = '/api/v1/get-hackathon-list/past/'
        response=self.client.get(url)
        self.assertEqual(response.status_code,HTTP_200_OK)
    
    def test_future_hackathon_list(self):
        url = '/api/v1/get-hackathon-list/future/'
        response=self.client.get(url)
        self.assertEqual(response.status_code,HTTP_200_OK)