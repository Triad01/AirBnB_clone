#!/usr/bin/python3
"""Module contains the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents the amenity model"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
