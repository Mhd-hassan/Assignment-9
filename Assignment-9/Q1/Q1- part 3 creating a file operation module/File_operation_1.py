# Name: Muhammad Hassan Noorsumar
# Day: Monday
# Date: 17/07/2023
# Sub: Python
# Title: Assignment-9 
# Lets start
# Q1. Create a module consisting of class holding various data members and member functions. (class can be on various file operations or mathematical operations or string operations)

import File_Operation
file_op = File_Operation.FileOperations("example.txt")
file_op.write_file("Hello, world!")
file_op.append_file("\nWelcome to file operations.")
content = file_op.read_file()
print("File content:", content)
file_op.delete_file()

"""
Output of FileOperations:
File written successfully!
Content appended to file successfully!
File content: Hello, world!
Welcome to file operations.
File deleted successfully!
"""