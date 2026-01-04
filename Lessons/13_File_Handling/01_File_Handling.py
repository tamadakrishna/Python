# File Handling in Python

import os

# Get the current working directory like this script is executed
# print("CWD:", os.getcwd())

# Get the location of the python script
# print("Script location:", os.path.abspath(__file__))



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# load students.txt from the same directory as this script

FILE_PATH = os.path.join(BASE_DIR, "students.txt")

# Opening a file
file = open(FILE_PATH, "r")  # Open a file in read mode


# Reading from a file
content = file.read()  # Read the entire content of the file
print("File Content:")
print(content)
file.close()  # Close the file after reading


WRITE_PATH = os.path.join(BASE_DIR, "output.txt")
# Writing to a file
file = open(WRITE_PATH, "w")  # Open a file in write mode (creates the file if it doesn't exist)
file.write("Hello, World!\n")  # Write a string to the file
file.write("This is a new line.\n")
file.close()  # Close the file after writing


# Appending to a file
file = open(WRITE_PATH, "a")  # Open a file in append mode
file.write("This line is appended.\n")  # Append a string to the file
file.close()  # Close the file after appending

# Using 'with' statement for file handling
with open(WRITE_PATH, "r") as file:  # Open the file in read mode
    content = file.read()  # Read the entire content of the file
    print("Updated File Content:")
    print(content)  # Print the content read from the file  
# No need to explicitly close the file when using 'with' statement



# Reading file line by line
with open(FILE_PATH, "r") as file:
    print("Reading file line by line:")
    for line in file:
        print(line.strip())  # Print each line without extra newline characters 
# strip() removes leading/trailing whitespace including newlines


# Checking if a file exists
if os.path.exists(WRITE_PATH):
    print(f"The file {WRITE_PATH} exists.")
else:
    print(f"The file {WRITE_PATH} does not exist.")

# Deleting a file
# os.remove(WRITE_PATH)
# print(f"The file {WRITE_PATH} has been deleted.") 
# Uncomment the above two lines to delete the file created earlier



