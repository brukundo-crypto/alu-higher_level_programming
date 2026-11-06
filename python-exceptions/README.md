# Python - Exceptions

Functions that handle and raise exceptions, written without importing any
module.

## What is in here

| File | Description |
|---|---|
| 0-safe_print_list.py | Prints x elements of a list and returns how many printed |
| 1-safe_print_integer.py | Prints a value as an integer, returning True or False |
| 2-safe_print_list_integers.py | Prints only the integers of the first x elements |
| 3-safe_print_division.py | Divides two integers and reports the result in finally |
| 4-list_division.py | Divides two lists element by element, naming each failure |
| 5-raise_exception.py | Raises a TypeError |
| 6-raise_exception_msg.py | Raises a NameError carrying a message |

## Notes on the exception handling

- Task 0 catches `IndexError` and stops, because x may exceed the list.
- Task 2 deliberately does **not** catch `IndexError`: the task requires that
  exception to surface when x exceeds the list, so only `ValueError` and
  `TypeError` are caught to skip non-integers in silence.
- Tasks 3 and 4 use `finally` so the result is recorded whether or not the
  division succeeded.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- Files begin with `#!/usr/bin/python3` and end with a new line
- All files are executable
- Code follows pycodestyle 2.7
- No modules are imported anywhere in this directory
- `len()` is not used in tasks 0 and 2, and `type()` is not used in task 1
