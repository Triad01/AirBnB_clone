#!/usr/bin/python3
"""Module contains class for the state model"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents the state model"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
