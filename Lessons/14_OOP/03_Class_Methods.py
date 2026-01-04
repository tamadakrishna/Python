# Different types of class methods in Python OOP

class Student:
    school_name = "SREE KRISHNA GRAMMAR SCHOOL"  # Class variable shared by all instances

    # Constructor to initialize the object
    def __init__(self, name, age):
        self.name = name  # Instance variable for name
        self.age = age    # Instance variable for age

    # Instance method to display student details
    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

    # Class method to get the school name
    @classmethod
    def get_school_name(cls):
        return cls.school_name

    # Static method to check if a student is adult
    @staticmethod
    def is_adult(age):
        return age >= 18

# Creating an object of the Student class
student1 = Student("Krishna", 20) 
student1.display_info()  # Calling the instance method to display info
print(f"School Name: {Student.get_school_name()}")  # Calling the class method
print(f"Is student adult? {'Yes' if Student.is_adult(student1.age) else 'No'}")  # Calling the static method

