# Package

A package in Python is a directory (folder) that contains multiple modules and possibly sub-packages, used to organize related code.



11_Packages/
│
├── main.py
└── my_pack/
    ├── __init__.py
    ├── module1.py
    └── module2.py

__init__.py tells Python that mypackage is a package.

    1. Mark directory as a package
    2. Initialize package code
    3. Control what is imported

__all__ affects only this statement:
        from my_pack import *


## Import Packages

## Different Ways to Import from Packages

1. Import entire module
2. Import module using alias
3. Import specific function
4. Import all (not recommended)

## Nested Packages (Sub-Packages)
## Note: Not created yet, try your own
11_Packages/
│
├── main.py
└──── school/
    ├── __init__.py
    ├── students/
    │   ├── __init__.py
    │   └── student.py
    └── teachers/
        ├── __init__.py
        └── teacher.py


__all__ in Packages

Used to control what gets imported using *
__all__ = ["module1"]