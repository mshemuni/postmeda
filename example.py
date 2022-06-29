from pmweather import Country
from pmweather import Weather


# Create a country object
canada = Country("city.list.json")
# Print list of available cities
print(canada.cities)

# Get a city (toronto)
toronto = canada.get_city_info("toronto")
# print(toronto)
# Get weather for toronto
w = Weather(toronto)
# print(w.current_by_name())
# print(w.current_by_coordinates())
w = w.current_by_coordinates()
print(w.get("coord").get("lon"))
print(w.get("coord").get("lat"))
