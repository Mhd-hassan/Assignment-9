# Name: Muhammad Hassan Noorsumar
# Day: Monday
# Date: 17/07/2023
# Sub: Python
# Title: Assignment-9 
# Lets start
# Q3. Also in the same file, create a user defined exception and implement it.

from Q3 import MathOperations,MathError

math_ops =MathOperations() # Create an instance of MathOperations

sum_result = math_ops.add(10, 5) # Perform various mathematical operations
difference_result = math_ops.subtract(10, 5)
product_result = math_ops.multiply(10, 5)

try:
    division_result = math_ops.divide(10, 2)
    print("Division:", division_result)
except MathError as error:
    print(error)

"""
Output of MathOperations and Matherror-1:
MathError: Division by zero is not allowed.
"""

"""
Output of MathOperations and Matherror-2:
Division: 5.0
"""