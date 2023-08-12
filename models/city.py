#!/usr/bin/python3
"""Module which breaksdown a city class"""
from models.base_model import BaseModel



class City(BaseModel):
    """ The city class, contains state ID and name
    Attribute:
        state_id (str): The state id.
        name (str): The name of the city.
    """
    name = ""
    state_id = ""
