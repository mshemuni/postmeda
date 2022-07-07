import json

from .city import City
from .errors import CityNotFound

from typing import List


class Country:
    def __init__(self, file: str) -> None:
        """
        constructor method

        :param file: A file to read data of all cities available in Canada
        """
        self.file = file
        self.city_data = self.__read_canada()

    def __read_canada(self) -> List[City]:
        """
        returns a list of City objects to each city in self.file
        :return: List of cities
        """
        with open(self.file, 'r', encoding="utf8") as j:
            world_cities = json.loads(j.read())
            return [
                City(
                    city.get("id"), city.get("name"),
                    city.get("coord").get("lon"), city.get("coord").get("lat"),
                    city.get("country"), city.get("state")

                )
                for city in world_cities
                if city.get("country") == "CA"
            ]

    @property
    def cities(self) -> List[str]:
        """
        Returns list of cities available in self.file (sorted)

        :return: list of cities
        """
        return sorted(
            [
                each.name
                for each in self.city_data
            ]
        )

    def get_city_info(self, city: str) -> City:
        """
        Returns City object of a given city name

        :param city: City name
        :return: a city object
        """
        for each in self.city_data:
            if each.name.upper().strip() == city.upper().strip():
                return each
        raise CityNotFound(f"No such city ({city})")
