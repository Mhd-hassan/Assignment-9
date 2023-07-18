# Name: Muhammad Hassan Noorsumar
# Day: Monday
# Date: 17/07/2023
# Sub: Python
# Title: Assignment-9 
# Lets start
# Q1. Create a module consisting of class holding various data members and member functions. (class can be on various file operations or mathematical operations or string operations)

# Example-1

import Assignment_9
emp=Assignment_9.Employee("Hassan","DS,AI,ML,Full Stack Developer")
emp.show()

# """
# Output of Example-1:
# Employee name is :  Hassan
# Employee position is :  DS,AI,ML,Full Stack Developer
# """

# Example-2

from Assignment_9 import *
Assignments() # calling a function
print(location) # printing the variable
emp=Employee("Hassan","DS,AI,ML,Full Stack Developer") # calling class
emp.show()

# """
# Output of Example-2:
# Assignment 9
# India
# Employee name is :  Hassan
# Employee position is :  DS,AI,ML,Full Stack Developer
# """

# Example-3

import Assignment_9 as a
a.Assignments() # calling the function
print(a.location) # calling the variable
emp=a.Employee("Hassan","DS,AI,ML,Full Stack Developer")
emp.show()

"""
Output of Example-3:
Assignment 9
India
Employee name is :  Hassan
Employee position is :  DS,AI,ML,Full Stack Developer
"""

"""
Entire output:

Employee name is :  Hassan
Employee position is :  DS,AI,ML,Full Stack Developer

Assignment 9
India
Employee name is :  Hassan
Employee position is :  DS,AI,ML,Full Stack Developer

Assignment 9
India
Employee name is :  Hassan
Employee position is :  DS,AI,ML,Full Stack Developer
"""