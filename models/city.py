#!/usr/bin/python3
"""Module contains the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents the city model"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        state_id = ""
        self.name = ""
