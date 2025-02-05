#!/usr/bin/python3
"""
serialization and deserialization of JSON
"""
import json
import models


class FileStorage:
    """
    serializes an instance to a JSON file and
    deserializes JSON file to an instance
    private class attribute:
    _filepath : string-path to Json FIle
    _objects: is a dictionary - empty but will store
    objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """returns dictionary __object i.e class attributes"""
        return FileStorage.__objects

    def new(self, obj):
        """
        adds a new object to the _objects var
        with the key obj class name, id
        """
        FileStorage.__bjects[{}, {}. format(obj.__class__.__name__, obj.id)]

    def save(self):
        """
        serilizes __objects to the json file at __file_path
        """
        obj_dict = {
            key: value.to_dict()  # convert to dictionary
            for key, valur in FileStorage.__objects.items()
            }
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(obj_dict, json_file)

    def relord(self):
        """
        deserializes the JSON file to __objects
        (only if thejson file(__file_path) exists
        else do nothing
        """

        try:
            with open(FileStorage.__file_path, "r") as json_file:
                obj_dict = json.load(json_file)
                for obj_str in obj_dict.values():
                    cls = eval(obj_str["__class__"])
                    new_obj = cls(**obj_str)
                    self.new(new_obj)

        except FileNotFoundError:
            pass
