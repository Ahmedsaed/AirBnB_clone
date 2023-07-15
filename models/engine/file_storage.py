#!/usr/bin/python3
"""File Storage Module"""

import json
import os


class FileStorage():
    """File Storage Class Representation"""

    __file_path = "storage_file.json"
    __objects = {}

    def __init__(self):
        """Init instance"""
        pass

    def all(self):
        """return storage objects"""
        return FileStorage.__objects

    def new(self, obj):
        """add new object to file storage"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """save objects to file"""
        with open(FileStorage.__file_path, "w") as file:
            storage_dict = {k: v.to_dict()
                            for k, v in FileStorage.__objects.items()}
            json.dump(storage_dict, file)

    def classes(self):
        """map class names to python class"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }

        return classes

    def reload(self):
        """reload objects from file"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as file:
            storage_dict = json.load(file)
            storage_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in storage_dict.items()}
            FileStorage.__objects = storage_dict
