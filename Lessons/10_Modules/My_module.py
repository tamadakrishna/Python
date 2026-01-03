# my_module.py

# A variable
greeting = "Hello from my_module!"

def greet():
    print("Hello, welcome to my_module!")

# Use of __name__ prevents code from running on import
if __name__ == "__main__":
    print("This is my_module being run directly.")

