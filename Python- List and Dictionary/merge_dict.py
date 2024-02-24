# 7. Write a Python script to merge two Python dictionaries.

dic1={'a': 23, 'b': 45, 'c': 10, 'd': 5}

dic2={'w': 23, 'x': 24, 'y': 25, 'z': 26}

res=dict()
res.update(dic1)
res.update(dic2)

print(res)