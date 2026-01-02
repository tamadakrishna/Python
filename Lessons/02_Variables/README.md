# Variables 
variables in Python are used to store data values.

# In Python, you don’t need to declare a type. You just assign a value using =

### Example

name = "Krishna"    # stores a string
age = 22            # stores an integer
height = 182.0      # stores a float
is_student = True   # stores a boolean


Here:
name, age, height, is_student → variables
"Krishna", 22, 182.0, True → values stored in the variables



# Rules for variable names
1. Must start with a letter or underscore _.
2. Can only contain letters, numbers, and underscores.
3. Case-sensitive: age ≠ Age
4. Cannot be a Python keyword (like if, for, class, etc.)



# Reassigning variables
-> You can change the value stored in a variable anytime:
Refer 01_Variables.py



# Multiple assignments
Python allows you to assign multiple variables in one line:
Refer 01_Variables.py


# Dynamic typing
Python variables change type automatically if you assign a different type
Refer 01_Variables.py


# Type Checking
In Python, you can check the type of a variable using the type() function.
Refer 02_Type_Checking.py


# Type Conversion (Casting)
conversion one type to another is called type casting.

| Function  | Converts to | Example                         |
| --------- | ----------- | ------------------------------- |
| `int()`   | Integer     | `int(3.14)` → `3`               |
| `float()` | Float       | `float(10)` → `10.0`            |
| `str()`   | String      | `str(10)` → `"10"`              |
| `bool()`  | Boolean     | `bool(0)` → `False`             |
| `list()`  | List        | `list("abc")` → `['a','b','c']` |
| `tuple()` | Tuple       | `tuple([1,2,3])` → `(1,2,3)`    |
| `set()`   | Set         | `set([1,1,2])` → `{1,2}`        |

Refer 03_Type_Conversion.py
