# Python - Input/Output

Reading and writing text files, moving objects in and out of JSON, and one
interview-style exercise.

## What is in here

| File | Description |
|---|---|
| 0-read_file.py | Reads a UTF-8 text file and prints it to stdout |
| 1-write_file.py | Writes a string to a file and returns the character count |
| 2-append_write.py | Appends a string to a file and returns the count added |
| 3-to_json_string.py | Returns the JSON representation of an object |
| 4-from_json_string.py | Returns the object described by a JSON string |
| 5-save_to_json_file.py | Writes an object to a file as JSON |
| 6-load_from_json_file.py | Builds an object from a JSON file |
| 7-add_item.py | Adds the command line arguments to add_item.json |
| 8-class_to_json.py | Returns the dictionary description of an instance |
| 9-student.py | A Student class with to_json() |
| 10-student.py | Adds an attribute filter to to_json() |
| 11-student.py | Adds reload_from_json() |
| 12-pascal_triangle.py | Returns Pascal's triangle of n rows |

## Notes

- Every file operation uses `with`, so the file is closed even if something
  raises part way through.
- Tasks 0, 1, 2, 8, 9, 10, 11 and 12 import nothing. The JSON tasks import
  `json`, and `7-add_item.py` imports `sys` and reuses tasks 5 and 6 through
  `__import__`.
- `7-add_item.py` catches `FileNotFoundError` so the first run starts from an
  empty list instead of failing.
- `class_to_json` returns a copy of `__dict__`, so a caller changing the
  returned dictionary does not quietly change the object.
- Only instance attributes appear in `__dict__`. A class attribute shows up
  only once an instance has assigned to it, which is why `score` appears for
  `MyClass` after `win()` runs.
- `to_json(attrs)` keeps every attribute unless `attrs` really is a list of
  strings, and silently ignores names the student does not have.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- Files begin with `#!/usr/bin/python3` and end with a new line
- All files are executable
- Code follows pycodestyle 2.7
- Modules, classes and methods carry docstrings

