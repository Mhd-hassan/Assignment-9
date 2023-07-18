# Name: Muhammad Hassan Noorsumar
# Day: Monday
# Date: 17/07/2023
# Sub: Python
# Title: Assignment-9 
# Lets start
# Q3. Also in the same file, create a user defined exception and implement it.

class MathOperations:
    def __init__(self):
        pass
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise MathError("Division by zero is not allowed.")


class MathError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return f"MathError: {self.message}"

"""
Output of MathOperations and Matherror-1:
MathError: Division by zero is not allowed.
"""

"""
Output of MathOperations and Matherror-2:
Division: 5.0
"""