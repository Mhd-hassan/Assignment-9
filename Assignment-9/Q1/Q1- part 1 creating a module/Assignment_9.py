# Name: Muhammad Hassan Noorsumar
# Day: Monday
# Date: 17/07/2023
# Sub: Python
# Title: Assignment-9 
# Lets start
# Q1. Create a module consisting of class holding various data members and member functions. (class can be on various file operations or mathematical operations or string operations)

# Example-1

def Assignments (): # Defining a function
    print("Assignment 9")
location="India" # Definign a variable
class Employee():
    def __init__(self,name,position):
        self.name=name
        self.position=position
    def show(self):
        print("Employee name is : ",self.name)
        print("Employee position is : ",self.position)

"""
Output of Example-1:
Employee name is :  Hassan
Employee position is :  DS,AI,ML,Full Stack Developer
"""

"""
Output of Example-2:
Assignment 9
India
Employee name is :  Hassan
Employee position is :  DS,AI,ML,Full Stack Developer
"""

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