# List Data Structure in Python

# Allows duplicates and maintains order of elements.
# Grow and shrink dynamically.

# List of numbers
numbers = [10, 20, 30, 40]

# Mixed list
mixed_list = [10, "Hello", True, 3.14]

print("Numbers:", numbers)
print("Mixed List:", mixed_list)

'''
Accessing List Elements
Indexing → access a single element by position (starts at 0)
Negative indexing → access from the end (-1 = last element)
Slicing → access a range of elements
'''
fruits = ["apple", "banana", "cherry", "orange"]

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Slice [1:3]:", fruits[1:3])  # From index 1 to 2


# Modifying Lists
# Adding Elements

fruits = ["apple", "banana"]

fruits.append("cherry")       # Add at the end
fruits.insert(1, "orange")    # Add at specific index
fruits.extend(["kiwi", "mango"])  # Add multiple elements

print("After adding:", fruits)


# Removing Elements
fruits.remove("banana")  # Remove by value
popped = fruits.pop()    # Remove last element
del fruits[0]            # Remove by index
fruits.clear()           # Remove all elements

print("After removing:", fruits)

# Updating Elements
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"   # Change "banana" to "orange"
print("Updated list:", fruits)


# Iterating Through a List

# Using for loop
for fruit in fruits:
    print(fruit)

# Using while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1



# Nested Lists (2D Lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Element at row 2, col 3:", matrix[1][2])  # 6


