# Output using print() function

name = "Krishna"
age = 25

print(name)
print(age)



# Formatted Output
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {0} and I am {1} years old.".format(name, age))
# {0} and {1} are positional arguments  
print("My name is %s and I am %d years old." % (name, age))
print("My name is " + name + " and I am " + str(age) + " years old.")




# Multi-line Output
print("""This is a multi-line
output example.
You can write text
across multiple lines.""")




# Using sep and end parameters
print("Hello", "World", sep=", ", end="!\n")
print("This is the second line.")   




# Escape Sequences
print("This is a line with a newline character.\nSee?")
print("This is a line with a tab character.\tSee?")
print("This is a line with a backslash character.\\ See?")
print("He said, \"Hello!\"")
print('It\'s a beautiful day!') 



# Raw Strings
# No escape sequences will be processed
print(r"This is a raw string.\nNo escape sequences are processed.\tSee?")   



# Printing without a newline
print("This is printed without a newline.", end=" ")
print("See, it's on the same line.")




# Using the format() method for advanced formatting
number = 1234.56789
print("Formatted number: {:.2f}".format(number))  # 2 decimal places
print("Number with commas: {:,}".format(number))   # Comma as thousand separator
print("Percentage: {:.2%}".format(0.756))         # Percentage format





# Using f-strings for advanced formatting
pi = 3.141592653589793
print(f"Pi rounded to 3 decimal places: {pi:.3f}")
print(f"Pi in scientific notation: {pi:.2e}")   
print(f"Pi with leading zeros: {pi:08.3f}")




# Combining multiple features
name = "Krishna"
score = 95.6789
print(f"Student: {name}\nScore: {score:.2f}\nStatus: {'Pass' if score >= 60 else 'Fail'}")  


