import unittest
from pmweather import Country, Weather
from pmweather.errors import CityNotFound, ServerError


class TestCountry(unittest.TestCase):
    def test_init(self):
        canada = Country("city.list.json")

        self.assertEqual(len(canada.cities), 3302)

    def test_cities(self):
        canada = Country("city.list.json")
        self.assertEqual(canada.cities[0], "Abbey")

    def test_get_city_info(self):
        canada = Country("city.list.json")

        # Get toronto
        toronto = canada.get_city_info("toronto")

        self.assertEqual(toronto.name, "Toronto")
        self.assertAlmostEqual(toronto.lat, 43.700111)
        self.assertAlmostEqual(toronto.lng, -79.416298)

    def test_get_city_info_case(self):
        canada = Country("city.list.json")

        # Get toronto case insensitive
        toronto2 = canada.get_city_info("ToRONto")

        self.assertEqual(toronto2.name, "Toronto")
        self.assertAlmostEqual(toronto2.lat, 43.700111)
        self.assertAlmostEqual(toronto2.lng, -79.416298)

    def test_get_city_info_spaces(self):
        canada = Country("city.list.json")

        # Get toronto white-spaces
        toronto3 = canada.get_city_info("   ToRONto        ")

        self.assertEqual(toronto3.name, "Toronto")
        self.assertAlmostEqual(toronto3.lat, 43.700111)
        self.assertAlmostEqual(toronto3.lng, -79.416298)

    def test_get_city_info_error(self):
        canada = Country("city.list.json")
        # Get toronto2. Must raise error (CityNotFound)
        with self.assertRaises(CityNotFound):
            toronto3 = canada.get_city_info("toronto2")


class TestWeather(unittest.TestCase):
    def test_init(self):
        canada = Country("city.list.json")

        # Get toronto
        toronto = canada.get_city_info("toronto")

        # Create weather object
        weather = Weather(toronto)

        # Check if city on weather object is as same as given city
        self.assertEqual(weather.city, toronto)

    def test_current_by_coordinates(self):
        canada = Country("city.list.json")

        # Get toronto
        toronto = canada.get_city_info("toronto")

        # Create weather object
        weather = Weather(toronto)
        # Get weather for toronto by coordinates
        weather_data = weather.current_by_coordinates()

        # Since weather value changes we only can check
        # if the coordinates retrieved from openweather map is correct
        self.assertAlmostEqual(weather_data.get("coord").get("lon"), -79.4163)
        self.assertAlmostEqual(weather_data.get("coord").get("lat"), 43.7001)

    def test_current_by_name(self):
        canada = Country("city.list.json")

        # Get toronto
        toronto = canada.get_city_info("toronto")

        # Create weather object
        weather = Weather(toronto)
        # Get weather for toronto by name
        weather_data = weather.current_by_name()

        # Since weather value changes we only can check
        # if the coordinates retrieved from openweather map is correct
        self.assertAlmostEqual(weather_data.get("coord").get("lon"), -79.4163)
        self.assertAlmostEqual(weather_data.get("coord").get("lat"), 43.7001)

    def test_current_by_name_wrong_api(self):
        canada = Country("city.list.json")

        # Get toronto
        toronto = canada.get_city_info("toronto")

        # Create weather object
        weather = Weather(toronto)
        # Get weather for toronto by name
        weather_data = weather.current_by_name()

        # Check for server error.
        # We can change the API KEY and send a request. We should get 401 server error
        weather.API_KEY = "Some Gibberish Things"
        with self.assertRaises(ServerError):
            weather_data2 = weather.current_by_name()


if __name__ == '__main__':
    unittest.main()
