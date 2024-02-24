# 9. Write a Python program to multiply all the items in a dictionary.

dic1={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'w': 5, 'x': 5, 'y': 5, 'z': 5}

prod=1

for _,value in dic1.items():
    prod *= value

print(prod)