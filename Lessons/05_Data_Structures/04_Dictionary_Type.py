# Dictionary Type in Python
# Key-value pairs
# Keys are unique and immutable
# Values can be of any data type and can be duplicated
# --------- Creating Dictionaries ---------
# Using curly braces
dict1 = {"name": "Krishna", "age": 23, "city": "Visakhapatnam"}

# Using dict() constructor
dict2 = dict([("name", "Kittu"), ("age", 25), ("city", "Visakhapatnam")])
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
# Empty dictionary
empty_dict = {}
print("Empty Dictionary:", empty_dict)
# --------- Accessing Dictionary Elements ---------
person = {"name": "Krishna", "age": 25, "city": "Visakhapatnam"}
print("Name:", person["name"])
print("Age:", person.get("age"))
# --------- Modifying Dictionaries ---------
# Adding/Updating Elements
person["email"] = "tamadakrishnaa@gmail.com"  # Add new key-value pair
person["age"] = 24                        # Update existing key
print("After adding/updating:", person)


# Removing Elements
del person["city"]            # Remove by key
removed_age = person.pop("age")  # Remove and return value
print("After removing:", person)


# Clearing the dictionary
person.clear()
print("After clearing:", person)


# --------- Iterating Through a Dictionary ---------
person = {"name": "Krishna", "age": 25, "city": "Visakhapatnam"}



# Iterating through keys
for key in person:
    print("Key:", key)



# Iterating through values
for value in person.values():
    print("Value:", value)



# Iterating through key-value pairs
for key, value in person.items():
    print("Key:", key, "Value:", value)



# --------- Nested Dictionaries ---------
employees = {
    "emp1": {"name": "Steve", "age": 30},
    "emp2": {"name": "Linus", "age": 40}
}
print("Employee 1 Name:", employees["emp1"]["name"])
print("Employee 2 Age:", employees["emp2"]["age"])  



# Creating a dictionary from two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined_dict = {k: v for k, v in zip(keys, values)}
print("Combined Dictionary:", combined_dict)    




# --------- Dictionary Methods ---------
person = {"name": "Krishna", "age": 25, "city": "Visakhapatnam"}
print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items()) 
person_copy = person.copy()
print("Copied Dictionary:", person_copy)    
person.update({"age": 46, "email": "tamadakrishnaa@gmail.com"})
print("After update:", person)
removed_item = person.popitem()
print("Popped Item:", removed_item) 
print("After popitem:", person)





# --------- Handling Missing Keys ---------
{"name": "Krishna", "age": 25}
# Using get() method
print("City (using get):", person.get("city", "Not Found"))

# Using setdefault() method
city = person.setdefault("city", "Unknown")
print("City (using setdefault):", city)
print("After setdefault:", person)  





# --------- Merging Dictionaries ---------
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 3, "z": 4}


# Using update() method
dict_a.update(dict_b)
print("After update:", dict_a)


# Using dictionary unpacking (Python 3.5+)
dict_c = {**dict_a, **dict_b}
print("After unpacking:", dict_c)   
