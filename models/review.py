#!/usr/bin/python3
"""Module contains the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents the Review model"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
