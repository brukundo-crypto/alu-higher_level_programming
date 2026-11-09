# Python - Classes and Objects

A Square class built up across seven tasks, from an empty class to one with
validated properties and a printable, offset representation.

## What is in here

| File | Description |
|---|---|
| 0-square.py | An empty Square class |
| 1-square.py | Adds a private instance attribute size, with no validation |
| 2-square.py | Validates size on instantiation, raising TypeError or ValueError |
| 3-square.py | Adds the public instance method area() |
| 4-square.py | Replaces direct access with a size property and setter |
| 5-square.py | Adds my_print(), which draws the square with # |
| 6-square.py | Adds a position property used as an offset when printing |

## Notes

- `size` is private so the class controls its type and value. From task 4 the
  getter and setter centralise that validation in one place.
- `__size` is name-mangled by Python to `_Square__size`, which is why it shows
  up under that name in `__dict__` and is not reachable from outside as
  `__size`.
- In `my_print()`, a size of 0 prints a single empty line. The vertical part of
  `position` prints genuinely empty lines, never lines padded with spaces.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- Files begin with `#!/usr/bin/python3` and end with a new line
- All files are executable
- Code follows pycodestyle 2.7
- Modules, classes and methods carry docstrings
- No modules are imported anywhere in this directory
