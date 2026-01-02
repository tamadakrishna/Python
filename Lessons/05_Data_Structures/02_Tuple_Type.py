# Tuple Type in Python
# Immutable sequence type

# --------- Creating Tuples ---------

# Parentheses
t1 = (1, 2, 3)

# Without parentheses (tuple packing)
t2 = 4, 5, 6

# Single element tuple (needs comma)
t3 = (7,)
print("Single element tuple:", t3, "Type:", type(t3))

# Empty tuple
empty = ()
print("Empty tuple:", empty)



# --------- Accessing Tuple Elements ---------

fruits = ("apple", "banana", "cherry", "orange")

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Slice [1:3]:", fruits[1:3])

# --------- Tuple Concatenation and Repetition ---------

t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2      # Concatenation
t4 = t1 * 2       # Repetition

print("Concatenated:", t3)
print("Repeated:", t4)



# --------- Membership Testing ---------

fruits = ("apple", "banana", "cherry", "orange")
print("apple" in fruits)  # True
print("grape" not in fruits)  # False



# --------- Iterating Through a Tuple ---------

for fruit in fruits:
    print(fruit)





# --------- Nested Tuples (2D Tuples) ---------
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("Element at row 2, col 3:", matrix[1][2])  # 6



# --------Converting Between Tuples and Lists-----------

# Tuple → List
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print("List:", lst)

# List → Tuple
lst2 = [5, 6, 7]
t2 = tuple(lst2)
print("Tuple:", t2)



# --------- Tuple Unpacking ---------
person = ("Krishna", 25, "Engineer")
name, age, profession = person
print(name, age, profession)

