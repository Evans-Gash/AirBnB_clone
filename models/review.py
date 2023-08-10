#!/usr/bin/python3
"""Module that will provide client reviews"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class representation of the reviews
        Attributes:
                place_id: empty string: the actual Place.id
                user_id: empty string: the actual User.id
                text: empty string
    """
    place_id = ""
    user_id = ""
    text = ""
