from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class City:
    """
    A dataclass to create city objects
    """
    id: int
    name: str
    lng: float
    lat: float
    country: str
    state: str = ""
