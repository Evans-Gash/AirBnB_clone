#!/usr/bin/python3
"""Component that derives from the BaseMode"""
from models.base_model import BaseModel



class Place(BaseModel):
    """class that reps the state
    Attributes:
    city_id: empty string: the actual City.id
    user_id: empty string: the actual User.id
    name:  empty-string
    description: empty-string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: list of str - empty list:
    the actual list of Amenity.id later
    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
