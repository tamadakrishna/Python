# Set Type in Python
# Unordered collection of unique elements
# No duplicate elements allowed
# Mutable - can add or remove elements

# --------- Creating Sets ---------


# Using curly braces
set1 = {1, 2, 3, 4}



# Using set() constructor
set2 = set([3, 4, 5, 6])
print("Set 1:", set1)
print("Set 2:", set2)



# Empty set
empty_set = set()
print("Empty Set:", empty_set)
# Note: {} creates an empty dictionary, not a set



# --------- Accessing Set Elements ---------
# Sets are unordered, so we cannot access elements by index
# We can iterate through the set
for element in set1:
    print("Element:", element)



# Membership testing
print(2 in set1)  # True
print(5 not in set1)  # True   



# --------- Modifying Sets ---------

# Adding Elements
set1.add(5)               # Add single element
set1.update([6, 7, 8])    # Add multiple elements
print("After adding:", set1)



# Removing Elements
set1.remove(3)  # Remove specific element (raises error if not found)
set1.discard(10)  # Remove element if present (no error if not found)
popped = set1.pop()    # Remove and return an arbitrary element
print("After removing:", set1)  




# Clearing the set
set1.clear()           
print("After clearing:", set1)  




# --------- Set Operations ---------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Union
C = A | B
print("Union:", C)
# Intersection
D = A & B
print("Intersection:", D)
# Difference
E = A - B
print("Difference (A - B):", E)
# Symmetric Difference
F = A ^ B
print("Symmetric Difference:", F)
