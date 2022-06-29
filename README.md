# Posmedia Weather App (pmweather)
This app was created within the scope of Coding challenge 
presented to Mohammad S.Niaei by [Postmedia](https://www.postmedia.com/) technical team.

## Back-end
The back-end consistes of two part. 
- Core
- API

### Core
Core is consists of three classes.

- City
- Country
- Weather


#### City
`City` is a dataclass. It provides `id`, `name`, `lng`, `lat`, `country` and `state` (if USA).

This data type would be used to obtain coordinates or city name to provide to [openweathermap](https://openweathermap.org/)'s API.

#### Country
`Country` is a class that get's a json file which has a certain schema and provides list of cities.

Using this information `Country` can return
- a `city` object by given name.
- list of available cities (Canadian cities).

#### Weather
Providing a `city` object Weather can return
- current weather of given city from openweathermap using city 
name or coordinates.
- `n` days forecats of given city by name or coordinates (requires a valid API KEY)
### API
The service was created using `Django` and `Django Ninja` and it provides an API.

The api has three endpoints.

- Available Cities `/api/cities/available`
- City information `/api/cities/{city}`
- Current Weather for given City `/api/weather/current/{city}`

see: [api/docs](api/docs)

## Front-end
Using API provided by `pmweather` a single page front-end was created using `jquery` and `bootstrap`

## Requirements
- `Django==4.0.5`
- `ninja==1.10.2.3`
- `orjson==3.7.5`
- `requests==2.28.0`

## Installation

First clone the project: 

`git clone https://github.com/mshemuni/postmeda.git`

Change directory to the project's root:

`cd postmeda/`

Install Requirements:

`pip install -r requirements.txt`

and run it by:

`python manage.py runserver`


## Author
Mohammad SHAMEONI NIAEI

m.shemuni@gmail.com

## Examples
`example.py`

### From terminal
Getting list of cities
```commandline
curl -X 'GET' \
  'http://127.0.0.1:8080/api/cities/available' \
  -H 'accept: */*' | jq
```

Getting a city's information
```commandline
curl -X 'GET' \
  'http://127.0.0.1:8080/api/cities/toronto' \
  -H 'accept: */*' | jq
```

Getting weather data of a given city name from openweathermap
```commandline
curl -X 'GET' \
  'http://127.0.0.1:8080/api/weather/current/toronto' \
  -H 'accept: */*' | jq
```
>Note:
> 
> the `jq` is optional for pretty viewing on terminal

## Tests
### Core
`unittest`s are done for core library using `test_core.py`

Simply run the file.

>Note:
> 
> Since `City` is a `dataclass` I couldn't find a way to test it.

Tests are done for `Country` and `Weaher` classes



#### Test conditions:

For core test condition as below was tested:
- `TestCountry.test_init`: Check for number of cities available
- `TestCountry.test_cities`: Check if first element returned by `cities` method is `"Abbey"`
- `TestCountry.test_get_city_info`:  Check if the method returns correct element, from cities
- `TestCountry.test_get_city_info_case`:  Check if the method returns correct element, from cities even if the city name is given with different cases
- `TestCountry.test_get_city_info_spaces`:  Check if the method returns correct element, from cities even if there are redundant white-spaces before and after the city name
- `TestCountry.test_get_city_info_error`: Check if the method raises correct error if the given city name is not available

- `TestWeather.test_init`: Check if the given city is correct 
- `TestWeather.test_current_by_coordinates`: Check if the data returned by openweathermap belongs to the given city by checking the coordinates
- `TestWeather.test_current_by_name`: Chek-ck if the data returned by openweathermap belongs to the given city by checking the coordinates
- `TestWeather.test_current_by_name_wrong_api`: Check if the method raise correct error on wrong api key

### API

For the API, the tests are done differently. For api application of our django project we create a `test.py` file and 
running it by:

Simply run the code below in root directory.

```commandline
python manage.py test api
```

#### Test conditions:

- `APITestCase.test_available_cities`: Check if api returns correct number of element and if the first element is correct
- `APITestCase.test_get_city`: Check if the given city name returns correct city information
- `APITestCase.test_get_city_error`: Check if the error is returned by the api if wrong (not a city) city name is given
- `APITestCase.test_current_by_name`: Check if weather data contains correct coordinates for the given city
- `APITestCase.test_current_by_name_error`: Check if the error is returned by the api if wrong (not a city) city name is given


