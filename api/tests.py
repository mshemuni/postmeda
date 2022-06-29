from django.test import TestCase
from django.test import Client

ADDRESS = "http://127.0.0.1:8080"


class APITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_available_cities(self):
        """Test for available cities"""
        # Issue a GET request.
        response = self.client.get(f'{ADDRESS}/api/cities/available')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid number of cities.
        self.assertEqual(len(response.json()), 3302)
        # Check if first city is Abbey
        self.assertEqual(response.json()[0], "Abbey")

    def test_get_city(self):
        """Test for getting a single city"""
        response = self.client.get(f'{ADDRESS}/api/cities/toronto')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered json contains valid data.
        self.assertEqual(response.json().get("name"), "Toronto")
        self.assertAlmostEqual(response.json().get("lng"), -79.416298)
        self.assertAlmostEqual(response.json().get("lat"), 43.700111)

    def test_get_city_error(self):
        """Test for getting a single city with error"""
        response = self.client.get(f'{ADDRESS}/api/cities/toronto2')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check if the result is an error message.
        self.assertEqual(response.json().get("error"), "No such city (toronto2)")

    def test_current_by_name(self):
        """Test for getting current weather"""
        response = self.client.get(f'http://127.0.0.1:8080/api/weather/current/toronto')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Since values would change everytime we run this. We can check for coordinates
        self.assertAlmostEqual(response.json().get("coord").get("lon"), -79.4163)
        self.assertAlmostEqual(response.json().get("coord").get("lat"), 43.7001)

    def test_current_by_name_error(self):
        """Test for getting current weather with error"""
        response = self.client.get(f'{ADDRESS}/api/weather/current/toronto2')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check if the result is an error message.
        self.assertEqual(response.json().get("error"), "No such city (toronto2)")
