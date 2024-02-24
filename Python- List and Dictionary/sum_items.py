# 8.  Write a Python program to sum all the items in a dictionary.

dic1={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'w': 5, 'x': 5, 'y': 5, 'z': 5}

sum=0

for _,value in dic1.items():
    sum += value

print(sum)