#!/usr/bin/python3
"""Module responsible for defining the state class"""
from models.base_model import BaseModel



class State(BaseModel):
    """class-state
    Attribute:
            name(str): name of the actual state
    """
    name = ""
