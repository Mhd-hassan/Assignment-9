# Name: Muhammad Hassan Noorsumar
# Day: Monday
# Date: 17/07/2023
# Sub: Python
# Title: Assignment-9 
# Lets start
# Q1. Create a module consisting of class holding various data members and member functions. (class can be on various file operations or mathematical operations or string operations)

from String_Operation import StringOperations
input_string="Hassan"

string_op=StringOperations(input_string) # creating an instance of string operations

count_characters=string_op.count_characters() # perform string operations
count_words=string_op.count_words()
reverse_string=string_op.reverse_string()
uppercase_string=string_op.uppercase_string()
lowercase_string=string_op.lowercase_string()
capitalize_string=string_op.capitalize_string()

print("Input String: ",input_string) # print the results
print("Character count: ",count_characters)
print("Words Count",count_words)
print("Reverse String: ",reverse_string)
print("Uppercase String: ",uppercase_string)
print("Lowercase String: ",lowercase_string)
print("Capitalize String: ",capitalize_string)

"""
Output of Code:
Input String:  Hassan
Character count:  6
Words Count 1
Reverse String:  nassaH
Uppercase String:  HASSAN
Lowercase String:  hassan
Capitalize String:  Hassan
"""
