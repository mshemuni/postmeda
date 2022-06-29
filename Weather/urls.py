"""Weather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import orjson

from dataclasses import asdict

from django.contrib import admin
from django.urls import path

from ninja import NinjaAPI
from ninja.renderers import BaseRenderer

from . import views

from pmweather import Country, Weather
from pmweather import errors


class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        return orjson.dumps(data)


api = NinjaAPI(
    title="postmedia Weather App",
    version="0.0.1",
    description="This API and Front-end was created for the codding challenge given by postmedia.",
    renderer=ORJSONRenderer()

)


@api.get(
    "/cities/available", tags=["Cities"],
    description="Returns all available cities",
    summary="Get all available city names",

)
def available_cities(request):
    """
    Returns list of available cities
    """
    canada = Country("city.list.json")
    return canada.cities


@api.get(
    "/cities/{city}", tags=["Cities"],
    description="Returns all available cities",
    summary="Get information of a given city names",

)
def get_city(request, city: str):
    """
    Returns a city by name from available cities
    """
    canada = Country("city.list.json")
    try:
        return asdict(canada.get_city_info(city))
    except errors.CityNotFound as e:
        return {"error": str(e)}


@api.get(
    "/weather/current/{city}", tags=["weather"],
    description="Returns openweathermap data by given city name",
    summary="Get Weather by City Name (Canada only)",

)
def current_by_name(request, city: str):
    """
    Returns current weather for given city
    """
    canada = Country("city.list.json")
    try:
        wanted_city = canada.get_city_info(city)
    except errors.CityNotFound as e:
        return {"error": str(e)}

    weather = Weather(wanted_city)

    try:
        return weather.current_by_coordinates()
    except errors.ServerError as e:
        return {"error": str(e)}


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("all-cities", views.all_cities),
    path("api/", api.urls),
]
