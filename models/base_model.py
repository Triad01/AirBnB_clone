#!/usr/bin/python3
import uuid
from datetime import datetime
"""
    Module contains base model that defines all common
    attributes/methods for other classes
"""


class BaseModel():
    def __init__(self, *args, **kwargs):
        """initializing instances of base model with common attributes"""

        if kwargs:
            for (key, value) in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        date = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                        setattr(self, key, date)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Provides string representation of the instance object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}]"

    def save(self):
        """updates modification time for 'update_at' method"""
        self.update_at = datetime.now()

    def to_dict(self):
        """
            creates a dictionary representation
            suitable for serialization/deserialization
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
