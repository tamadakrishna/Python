# Import 01_Program module
import My_module   
# Accessing variable from My_module
print(My_module.greeting)

My_module.greet()  # Calling function from My_module

"""
Types of imports

Import specific function(s)
from My_module import greet
greet()

Import with alias
import My_module as mm
mm.greet()

Import all names (not recommended)
from My_module import *
greet() 

"""