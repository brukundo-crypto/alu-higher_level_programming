# Python - Inheritance

Functions that inspect how objects relate to classes, and a small geometry
hierarchy built with inheritance.

## What is in here

| File | Description |
|---|---|
| 0-lookup.py | Returns the list of attributes and methods of an object |
| 1-my_list.py | A list subclass that can print itself sorted |
| 2-is_same_class.py | True only if the object is exactly of the given class |
| 3-is_kind_of_class.py | True if the object is of the class or of a subclass |
| 4-inherits_from.py | True only if the object's class inherited from the given class |
| 5-base_geometry.py | An empty BaseGeometry class |
| 6-base_geometry.py | Adds area(), which raises an exception |
| 7-base_geometry.py | Adds integer_validator() |
| 8-rectangle.py | A Rectangle inheriting from BaseGeometry, with validated sides |
| 9-rectangle.py | Adds area() and the [Rectangle] description |
| 10-square.py | A Square inheriting from Rectangle |
| 11-square.py | Adds the [Square] description |
| tests/1-my_list.txt | Doctests for MyList |
| tests/7-base_geometry.txt | Doctests for BaseGeometry |

## Notes

- `integer_validator` checks with `type(value) is not int`, not `isinstance`.
  `bool` is a subclass of `int`, so `isinstance(True, int)` is True and a
  boolean would slip through; the project expects `Rectangle(4, True)` to
  raise `height must be an integer`.
- `is_same_class` compares the exact type, `is_kind_of_class` uses
  `isinstance` so subclasses count, and `inherits_from` uses `issubclass`
  while excluding the class itself.
- `Square` validates its size and stores it privately, then calls
  `super().__init__(size, size)` so the Rectangle half is set up once, in one
  place.
- `10-square.py` deliberately has no `__str__` of its own, which is why it
  prints `[Rectangle] 13/13`. Task 11 is where that is overridden.

## Running the tests

    python3 -m doctest tests/1-my_list.txt -v
    python3 -m doctest tests/7-base_geometry.txt -v

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- Files begin with `#!/usr/bin/python3` and end with a new line
- All Python files are executable
- Code follows pycodestyle 2.7
- Modules, classes and methods carry docstrings
- No modules are imported anywhere in this directory
