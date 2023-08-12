#!/usr/bin/python3
"""Elaborates/Defines a user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a user by details
    Attributes:
            email(str) - email of the person/user
            password(str) - password of the person/user
            first_name(str) - first_name of the person/user
            last_name(str) - last_name of person/user
            """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
