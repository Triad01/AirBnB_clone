#!/usr/bin/python3
"""Our first class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent the user model"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        password = ""
        first_name = ""
        last_name = ""
