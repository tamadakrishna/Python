# Function Annotation

# Annotating Parameters
# name: str indicates name should be a string
def greet(name: str):
    print("Hello", name)

greet("Krishna")

# Annotating Return Type
# -> int indicates the function returns an integer
def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))




# Multiple Parameters with Annotations
def student(name: str, age: int, marks: float) -> str:
    return f"{name}, Age: {age}, Marks: {marks}"

print(student("Krishna", 25, 90.5))



# Annotations with Default Values
# None means the function returns nothing
def greet(name: str = "User") -> None:
    print("Hello", name)

greet()
greet("Krishna")


# Annotations with *args
def total(*numbers: int) -> int:
    return sum(numbers)

print(total(1, 2, 3))


# Annotations with **kwargs
def profile(**info: str) -> None:
    for key, value in info.items():
        print(key, value)

profile(name="Krishna", city="Visakhapatnam")


# Accessing Annotations
# Python stores annotations in a dictionary:
def add(a: int, b: int) -> int:
    return a + b

print(add.__annotations__)

# {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}




# Annotations Do NOT Enforce Types
def add(a: int, b: int) -> int:
    return a + b

print(add("10", "20"))  # Works! (string concatenation)
# Python does NOT raise an error
