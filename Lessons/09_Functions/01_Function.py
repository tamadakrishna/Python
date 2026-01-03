# Functions
# def keyword is to define a function

# Simple function (no parameters)
def greet():
    print("Hello, World!")


# Function with parameters
def greet(name):
    """Function to greet a person by name."""
    print(f"Hello, {name}!")

greet("Krishna")  # Output: Hello, Krishna!


# Function with Return Value
def add(a, b):
    """Function to add two numbers."""
    return a + b   

result = add(5, 3)
print(f"The sum of 5 and 3 is {result}.")  # Output: The sum of 5 and 3 is 8.

# Function with Default Parameters
def greet(name="User"):
    print("Hello", name)

greet()
greet("Krishna")


# Function with keyword Arguments
def student(name, age):
    print(name, age)

student(age=25, name="Krishna")


# Variable-Length Arguments

# Multiple positional arguments
def sum_all(*args):
    return sum(args)   
total = sum_all(1, 2, 3, 4, 5)
print(f"The total sum is {total}.")  # Output: The total sum is 15.

# Multiple keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Krishna", age=25, city="Delhi")
# Lambda Functions
# Anonymous function to square a number
square = lambda x: x * x
print(f"The square of 5 is {square(5)}.")  # Output: The square of 5 is 25.

# Lambda function to add two numbers
add = lambda a, b: a + b
print(f"The sum of 10 and 15 is {add(10, 15)}.")  # Output: The sum of 10 and 15 is 25.


# Nested Functions
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()   

outer_function("Hello Krishna!")  # Output: Hello Krishna!

# Docstrings
def Demo(a, b):
    """This Comment acts as a docstring."""
    print("Hello, Docstring!")  
print(Demo.__doc__)  # Output: This Comment acts as a docstring.

