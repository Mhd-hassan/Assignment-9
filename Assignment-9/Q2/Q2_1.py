# Name: Muhammad Hassan Noorsumar
# Day: Monday
# Date: 17/07/2023
# Sub: Python
# Title: Assignment-9 
# Lets start
# Q2.  Import the above module created and try to implement their member functions.

from Q2 import MathOperations

math_ops = MathOperations() # Create an instance of MathOperations

sum_result = math_ops.add(10, 5) # Perform various mathematical operations
difference_result = math_ops.subtract(10, 5)
product_result = math_ops.multiply(10, 5)
division_result = math_ops.divide(10, 5)

print("Sum:", sum_result) # Print the results
print("Difference:", difference_result)
print("Product:", product_result)
print("Division:", division_result)

"""
Output of MathOperations:
Sum: 15
Difference: 5
Product: 50
Division: 2.0
"""