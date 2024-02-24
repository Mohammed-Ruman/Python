# 11. Write a Python program to sort a dictionary by key.

dic1={'z': 1, 'b': 2, 'c': 3, 'd': 4, 'w': 5, 'x': 5, 'y': 5, 'a': 5}

sort_dic1=sorted(dic1.items(),key=lambda x:x)

print(dict(sort_dic1))