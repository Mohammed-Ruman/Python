# 4. Write a Python script to check if a given key already exists in a dictionary. 

sample_dict={'a': 23, 'b': 45, 'c': 10, 'd': 5}

in_key=input("Enter the Key to search? ")

if in_key in sample_dict:
    print("Key already Present")
else:
    print("Key Not Present")