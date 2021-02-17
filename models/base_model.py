#!/usr/bin/python3
"""
base model
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
defines all common attributes from other classes:
    """
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """
        updates the public instance attribute with current datetime
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        a_dict = self.__dict__
        dict_str = {}
        for key, value in a_dict.items():
                if isinstance(value, datetime):
                    dict_str[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
                else:
                    dict_str[key] = value
        dict_str["__class__"] = self.__class__.__name__
        return dict_str
