#!/usr/bin/python3
"""Defines a Student class that can be saved and reloaded."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name: the student's first name.
            last_name: the student's last name.
            age: the student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary description of this Student.

        Args:
            attrs: a list of attribute names to keep. When it is not a
                list of strings, every attribute is returned.
        """
        if (type(attrs) is list and
                all(type(name) is str for name in attrs)):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace every attribute of this Student from a dictionary.

        Args:
            json: a dictionary of attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
