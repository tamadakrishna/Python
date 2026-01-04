# Class Definition in Python


class Student:
    # Constructor to initialize the object
    def __init__(self, name, age):
        self.name = name  # Instance variable for name
        self.age = age    # Instance variable for age

    # Method to display student details
    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}")


# Creating an object of the Student class
student1 = Student("Krishna", 20) 
student1.display_info()  # Calling the method to display info

