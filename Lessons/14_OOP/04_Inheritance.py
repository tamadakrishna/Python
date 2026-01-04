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






class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.subject = subject

    def display_info(self):
        super().display_info()  # Call the method from the parent class
        print(f"Subject: {self.subject}")






# Creating objects of Student and Teacher classes
student1 = Student("Krishna", 20, "Sciece")
teacher1 = Teacher("Pavan", 40, "Mathematics")
student1.display_info()
print()  # Just for a blank line
teacher1.display_info()





# Demonstrating isinstance and issubclass functions
print(f"\nIs student1 an instance of Student? {isinstance(student1, Student)}")
print(f"Is student1 an instance of Person? {isinstance(student1, Person)}")
print(f"Is Teacher a subclass of Person? {issubclass(Teacher, Person)}")
print(f"Is Student a subclass of Teacher? {issubclass(Student, Teacher)}")





# Multi-level Inheritance
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, research_topic):
        super().__init__(name, age, student_id)  # Call the constructor of the Student class
        self.research_topic = research_topic

    def display_info(self):
        super().display_info()  # Call the method from the Student class
        print(f"Research Topic: {self.research_topic}")


grad_student1 = GraduateStudent("Srinu", 25, "G67890", "Artificial Intelligence")
print()  # Just for a blank line

grad_student1.display_info()



# Demonstrating method resolution order (MRO)
print(f"\nMethod Resolution Order for GraduateStudent: {GraduateStudent.__mro__}")  
print(f"Method Resolution Order for Teacher: {Teacher.__mro__}")







# Using super() in multiple inheritance
class Athlete:
    def __init__(self, sport):
        self.sport = sport

    def display_sport(self):
        print(f"Sport: {self.sport}")

class StudentAthlete(Student, Athlete):
    def __init__(self, name, age, student_id, sport):
        Student.__init__(self, name, age, student_id)
        Athlete.__init__(self, sport)

    def display_info(self):
        Student.display_info(self)
        Athlete.display_sport(self)

student_athlete1 = StudentAthlete("Danie", 22, "SA11223", "Tennis")
print()  # Just for a blank line
student_athlete1.display_info()





# Demonstrating super() in multiple inheritance
class StudentAthleteSuper(Student, Athlete):
    def __init__(self, name, age, student_id, sport):
        super().__init__(name, age, student_id)
        Athlete.__init__(self, sport)

    def display_info(self):
        super().display_info()
        Athlete.display_sport(self)

student_athlete2 = StudentAthleteSuper("Ethan", 23, "SA33445", "Soccer")
print()  # Just for a blank line
student_athlete2.display_info()

# Demonstrating Method Resolution Order (MRO) with super()
print(f"\nMethod Resolution Order for StudentAthlete: {StudentAthlete.__mro__}")
print(f"Method Resolution Order for StudentAthleteSuper: {StudentAthleteSuper.__mro__}")
