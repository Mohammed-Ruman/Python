# 10) Write a Python program to get the class name of an instance in Python.

class Circle:
    pass

circle=Circle()

name=circle.__class__.__name__

print(name)