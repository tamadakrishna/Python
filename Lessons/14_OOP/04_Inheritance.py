# Inheritance example in Python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.student_id = student_id

    def display_info(self):
        super().display_info()  # Call the method from the parent class
        print(f"Student ID: {self.student_id}")

# Creating an object of the Student class
student1 = Student("Krishna", 20, "S12345")
student1.display_info()  # Calling the method to display info