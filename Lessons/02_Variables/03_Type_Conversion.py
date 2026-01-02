# This code demonstrates type conversion in Python.

# Integer to Float
x = 5
y = float(x)
print(y)       # 5.0
print(type(y)) # <class 'float'>


# Integer to String
x = "25"
y = int(x)
print(y + 5)   # 30

# Boolean Conversion
print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False (empty string is False)
print(bool("Hi"))    # True (non-empty string is True)

# List, tuple, and set conversion:
s = "hello"
print(list(s))   # ['h', 'e', 'l', 'l', 'o']
print(tuple(s))  # ('h', 'e', 'l', 'l', 'o')
print(set(s))    # {'h', 'e', 'l', 'o'}
# Note: Converting to set removes duplicates and does not maintain order.





# Important Notes
'''
1. You cannot convert incompatible types:

x = "abc"
y = int(x)  # Error! Cannot convert 'abc' to integer


2. Type conversion may lose information:
x = 3.99
y = int(x)
print(y)  # 3 (decimal lost)

'''

