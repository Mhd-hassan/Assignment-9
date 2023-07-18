# Name: Muhammad Hassan Noorsumar
# Day: Monday
# Date: 17/07/2023
# Sub: Python
# Title: Assignment-9 
# Lets start
# Q1. Create a module consisting of class holding various data members and member functions. (class can be on various file operations or mathematical operations or string operations)

from Mathematical_Operation import MathOperations

math=MathOperations() # creating an instance of MathOperations class

result=math.add(2,3) # perform addition

print("Addition of two number is : ",result) # output: Addition : 5

result=math.sub(4,2) # perform subtraction

print("Subtraction of two numbers is : ",result) # output: Subtraction: 2

result=math.mul(2,4) # perform multiplication

print("Multiplication of two number is : ",result) # Output: Multiplication: 8

result=math.div(4,4) # perform division

print("Division od two number is : ",result) # Output: Division: 1.0

"""
Output of MathOperations:
Addition of two number is :  5
Subtraction of two numbers is :  2
Multiplication of two number is :  8
Division od two number is :  1.0
"""