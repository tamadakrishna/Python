# Exception Handling 

## Basic try-except
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")




## Multiple exceptions
try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError:
    print("Division by zero error")
except ValueError:
    print("Invalid input")


# Single except for multiple exceptions
try:
    a = int(input())
    b = int(input())
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("Error occurred")


# Catching all exceptions
try:
    x = int("abc")
except Exception as e:
    print("Error:", e)
# Exception is the base class for most exceptions.
# Note: Not recommended to overuse — handle specific exceptions first.




# else Block in Exception Handling

# The else block runs only if no exception occurs.
try:
    x = int(input())
    y = int(input())
    print(x / y)
except ZeroDivisionError:
    print("Error")
else:
    print("Division successful")


# finally Block

# The finally block always executes, whether an exception occurs or not.
try:
    f = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    f.close()
    print("Closing file")
# Finally Used for cleanup (closing files, releasing resources)




# Raising Exceptions (raise)
# You can raise exceptions manually using the raise statement.
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    else:
        print("Valid age:", age)
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError as e:
    print("Error:", e)

# Custom Exception
