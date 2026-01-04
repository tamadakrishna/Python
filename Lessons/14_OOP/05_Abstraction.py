# Abstraction in OOP
from abc import ABC, abstractmethod

# Abstract base class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete class inheriting from Vehicle
class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

# Creating an object of the Car class
my_car = Car()
my_car.start()  # Output: Car started
my_car.stop()   # Output: Car stopped