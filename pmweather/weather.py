import requests

from .city import City
from .errors import ServerError


class Weather:
    def __init__(self, city: City) -> None:
        """
        Constructor method

        :param city: City to get weather
        """
        self.city = city
        self.API_KEY = "f0665395dee59e656b8a205b0d1931d2"
        self.count = 5
        self.units = "metric"

    def current_by_coordinates(self) -> dict:
        """
        Returns current weather of given city by its coordinates

        :return: Dictionary of weather
        """
        r = requests.get(f"https://api.openweathermap.org/data/2.5/"
                         f"weather?lat={self.city.lat}&lon={self.city.lng}&appid={self.API_KEY}&units={self.units}")

        if r.status_code == 200:
            return r.json()

        raise ServerError(r.status_code)

    def five_days_by_coordinates(self) -> dict:
        """
        Returns weather for self.count days of given city by its coordinates

        Requires correct API (For now it won't work)

        :return: Dictionary of weather
        """
        r = requests.get(f"api.openweathermap.org/data/2.5/forecast/"
                         f"daily?lat={self.city.lat}&lon={self.city.lng}&cnt={self.count}"
                         f"&appid={self.API_KEY}&units={self.units}")

        if r.status_code == 200:
            return r.json()

        raise ServerError(r.status_code)

    def current_by_name(self) -> dict:
        """
        Returns current weather of given city by its name

        :return: Dictionary of weather
        """
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={self.city.name}"
                         f"&appid={self.API_KEY}&units={self.units}")

        if r.status_code == 200:
            return r.json()

        raise ServerError(r.status_code)

    def five_days_by_name(self) -> dict:
        """
        Returns weather for self.count days of given city by its name

        Requires correct API (For now it won't work)

        :return: Dictionary of weather
        """
        r = requests.get(f"https://api.openweathermap.org/data/2.5/forecast/"
                         f"daily?q={self.city.name}&cnt={self.count}&appid={self.API_KEY}&units={self.units}")

        if r.status_code == 200:
            return r.json()

        raise ServerError(r.status_code)
