# Name: Muhammad Hassan Noorsumar
# Day: Monday
# Date: 17/07/2023
# Sub: Python
# Title: Assignment-9 
# Lets start
# Q1. Create a module consisting of class holding various data members and member functions. (class can be on various file operations or mathematical operations or string operations)

class FileOperations:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def read_file(self):
        try:
            with open(self.file_name, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print("File not found!")
    
    def write_file(self, content):
        try:
            with open(self.file_name, 'w') as file:
                file.write(content)
            print("File written successfully!")
        except IOError:
            print("Error writing to file!")
    
    def append_file(self, content):
        try:
            with open(self.file_name, 'a') as file:
                file.write(content)
            print("Content appended to file successfully!")
        except IOError:
            print("Error appending to file!")
    
    def delete_file(self):
        import os
        try:
            os.remove(self.file_name)
            print("File deleted successfully!")
        except FileNotFoundError:
            print("File not found!")
        except PermissionError:
            print("Permission denied!")

"""
Output of FileOperations:
File written successfully!
Content appended to file successfully!
File content: Hello, world!
Welcome to file operations.
File deleted successfully!
"""