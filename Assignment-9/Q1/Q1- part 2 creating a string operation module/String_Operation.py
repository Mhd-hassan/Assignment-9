# Name: Muhammad Hassan Noorsumar
# Day: Monday
# Date: 17/07/2023
# Sub: Python
# Title: Assignment-9 
# Lets start
# Q1. Create a module consisting of class holding various data members and member functions. (class can be on various file operations or mathematical operations or string operations)

class StringOperations:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def count_characters(self):
        return len(self.input_string)
    
    def count_words(self):
        words = self.input_string.split()
        return len(words)
    
    def reverse_string(self):
        return self.input_string[::-1]
    
    def uppercase_string(self):
        return self.input_string.upper()
    
    def lowercase_string(self):
        return self.input_string.lower()
    
    def capitalize_string(self):
        return self.input_string.capitalize()
    
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