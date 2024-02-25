# 12. Write a Python program to get the maximum and minimum value in a dictionary. 

dic1={'z': 1, 'b': 2, 'c': 3, 'd': 4, 'w': 5, 'x': 6, 'y': 7, 'a': 8}

# print(f"Max Value {dic1[max(dic1,key=dic1.get)]}")
# print(f"Min Value {dic1[min(dic1,key=dic1.get)]}")

max_value=0
min_value=float('inf')

for _,value in dic1.items():
    if(value>max_value):
        max_value=value
    if(value<min_value):
        min_value=value

print(f"Max Value {max_value}")
print(f"Min Value {min_value}")