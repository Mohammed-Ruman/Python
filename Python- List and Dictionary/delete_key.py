# 10. Write a Python program to remove a key from a dictionary. 

dic1={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'w': 5, 'x': 5, 'y': 5, 'z': 5}

in_key=input("Enter the key to delete? ")

print(f"Before Delete {dic1}")

del dic1[in_key]

print(f"After Delete {dic1}")