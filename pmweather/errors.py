class CityNotFound(Exception):
    """Raised when city not found"""
    pass


class ServerError(Exception):
    """Raised when openweathermap does not respond with 200"""
    pass
