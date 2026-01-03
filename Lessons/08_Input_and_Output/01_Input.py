# Input in Python
name = input("Enter your name: ")
print(f"Hello, {name}!")    

age = int(input("Enter your age: "))
print(f"You are {age} years old.")    


# Taking multiple inputs
num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
print(f"The sum of {num1} and {num2} is {num1 + num2}.")    


# Taking a list of inputs
numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
print(f"You entered the numbers: {numbers}")    



# Using input with default values
city = input("Enter your city (default is 'Unknown'): ") or "Unknown"
print(f"You live in {city}.")    
