#!/usr/bin/python3
"""This module defines the FileStorage class for managing
file storage for the HBNB clone project."""
import json


class FileStorage:
    """Class that serializes instances to a JSON file
    and deserializes JSON file to instances."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to __objects dictionary with key <obj_class_name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if the file exists"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }

        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    cls_name = val['__class__']
                    self.all()[key] = classes[cls_name](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()
