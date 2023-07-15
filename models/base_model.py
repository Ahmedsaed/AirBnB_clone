#!/usr/bin/python3
"""Base class module"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """Base model representation"""

    def __init__(self, *args, **kwargs) -> None:
        """init the instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """return the string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """update the instance"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return the dictionary representation of the instance"""
        ins_dict = {}
        ins_dict.update(self.__dict__)
        ins_dict["__class__"] = self.__class__.__name__
        ins_dict["created_at"] = ins_dict["created_at"].isoformat()
        ins_dict["updated_at"] = ins_dict["updated_at"].isoformat()
        return ins_dict
