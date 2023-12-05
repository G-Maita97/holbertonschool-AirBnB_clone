#!/usr/bin/python3
"""Creation of Model Base and import of libraries."""
from datetime import datetime
from uuid import uuid4
"""
Methods contained in the model base
class: "__init__",  "__str__", "save", "to_dict".

"""

class BaseModel:
    """Model base for the project."""
    def __init__(self, *args, **kwargs):
        """
        Initializer method.

        This method includes 3 attributes: "id", "created_at", "updated_at".

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.

        """
        if kwargs:
            """
            if statement to verify(through a for loop): 
                1.Existence of attribute "__class__" for exclusion from them.
                2.Set the created_at and updated_at values to a datetime object.
            """
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ 
        Returns the name of the class, the id attribute and 
        all content has the class dictionary (attributes).

        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update the value of update_at with the datetime current"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance 

        "__class__" = Added new key representing the class name of the object.

        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
