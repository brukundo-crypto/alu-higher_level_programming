# Python - More Classes and Objects

A Rectangle class built up across ten tasks, from an empty class to one with
class attributes, special methods, a static method and a class method.

## What is in here

| File | Description |
|---|---|
| 0-rectangle.py | An empty Rectangle class |
| 1-rectangle.py | Adds validated width and height properties |
| 2-rectangle.py | Adds area() and perimeter() |
| 3-rectangle.py | Adds __str__, which draws the rectangle with # |
| 4-rectangle.py | Adds __repr__, whose output can be passed to eval() |
| 5-rectangle.py | Adds __del__, printing Bye rectangle... on deletion |
| 6-rectangle.py | Adds the class attribute number_of_instances |
| 7-rectangle.py | Adds the class attribute print_symbol |
| 8-rectangle.py | Adds the static method bigger_or_equal() |
| 9-rectangle.py | Adds the class method square() |

## Notes

- `number_of_instances` is incremented with `Rectangle.number_of_instances`,
  not `self.number_of_instances`. Writing through `self` would create an
  instance attribute and leave the shared count untouched.
- `__str__` is read through `self.print_symbol`, so setting the symbol on one
  object overrides it for that object alone while the class default stands for
  the rest.
- `print_symbol` is wrapped in `str()`, which is what lets a list or any other
  type be used as the symbol.
- `bigger_or_equal` is a static method because it compares two rectangles and
  needs neither the instance nor the class; `square` is a class method because
  it builds and returns a new instance through `cls`.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- Files begin with `#!/usr/bin/python3` and end with a new line
- All files are executable
- Code follows pycodestyle 2.7
- Modules, classes and methods carry docstrings
- No modules are imported anywhere in this directory
