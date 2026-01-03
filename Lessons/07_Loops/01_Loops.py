# Loops

# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)



# While loop
i = 0
while i < 5:
    print(i)
    i += 1



# Break and continue statements
for i in range(10):
    if i == 5:
        break
    if i == 3:
        continue
    print(i)



# Nested loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")



# Using else with loops
for i in range(5):
    print(i)
else:
    print("Loop completed without break")



# Using enumerate function
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")



# Using zip function
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")
