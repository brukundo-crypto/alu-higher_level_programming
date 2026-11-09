# Python - Everything is object

Short answers about how Python handles objects, identity and mutability,
plus one function that copies a list.

## What is in here

| File | Question | Answer |
|---|---|---|
| 0-answer.txt | Function printing the type of an object | type |
| 1-answer.txt | Function giving the variable identifier | id |
| 2-answer.txt | a = 89, b = 100 — same object? | No |
| 3-answer.txt | a = 89, b = 89 — same object? | Yes |
| 4-answer.txt | a = 89, b = a — same object? | Yes |
| 5-answer.txt | a = 89, b = a + 1 — same object? | No |
| 6-answer.txt | s2 = s1, then s1 == s2 | True |
| 7-answer.txt | s2 = s1, then s1 is s2 | True |
| 8-answer.txt | Two equal strings, == | True |
| 9-answer.txt | Two equal strings, is | False |
| 10-answer.txt | Two equal lists, == | True |
| 11-answer.txt | Two equal lists, is | False |
| 12-answer.txt | l2 = l1, then l1 == l2 | True |
| 13-answer.txt | l2 = l1, then l1 is l2 | True |
| 14-answer.txt | append through an alias | [1, 2, 3, 4] |
| 15-answer.txt | rebinding with + | [1, 2, 3] |
| 16-answer.txt | incrementing an int inside a function | 1 |
| 17-answer.txt | appending to a list inside a function | [1, 2, 3, 4] |
| 18-answer.txt | reassigning a parameter inside a function | [1, 2, 3] |
| 19-copy_list.py | Function returning a copy of a list | — |
| 20-answer.txt | a = () — a tuple? | Yes |
| 21-answer.txt | a = (1, 2) — a tuple? | Yes |
| 22-answer.txt | a = (1) — a tuple? | No |
| 23-answer.txt | a = (1, ) — a tuple? | Yes |
| 24-answer.txt | a = (1), b = (1), a is b | True |
| 25-answer.txt | a = (1, 2), b = (1, 2), a is b | False |
| 26-answer.txt | a = (), b = (), a is b | True |
| 27-answer.txt | a = a + [5] keeps the same id? | No |
| 28-answer.txt | a += [4] keeps the same id? | Yes |

## The ideas behind the answers

- **== compares value, is compares identity.** Two separate lists holding the
  same numbers are equal but not the same object.
- **Small integers are cached.** CPython keeps one object for every integer
  from -5 to 256, so two variables set to 89 share it.
- **Assignment never copies.** `b = a` points a second name at the same
  object, which is why appending through one name is visible through the
  other.
- **Mutating differs from rebinding.** `append` and `+=` change the existing
  list, keeping its id. `l1 = l1 + [4]` builds a new list and points the name
  at it, leaving anything else that referenced the old list untouched.
- **Arguments are passed by object reference.** A function can mutate a list
  it is handed, but reassigning the parameter only rebinds the local name.
- **Commas make tuples, not brackets.** `(1)` is just the integer 1; `(1, )`
  is a one-element tuple. The empty tuple `()` is a single shared object in
  CPython.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- Answer files contain one line and end with a new line
- `19-copy_list.py` begins with `#!/usr/bin/python3`, is at most 3 lines, and
  is executable
- No modules are imported anywhere in this directory
