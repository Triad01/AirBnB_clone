#!/usr/bin/python3
"""Our first class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent the user model"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
