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

    # creating a BaseModel from dictionary
    def __init__(self, *args, **kwargs):
        """initializing an instance"""
        TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, TIME_FORMAT)
                elif key == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)
        

    def __str__(self):
        """
        returns the string representation of a class
        """
        
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """
        updates the public instance attribute with current datetime
        """
        self.update_at = datetime.now()
        models.storage.save()

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
