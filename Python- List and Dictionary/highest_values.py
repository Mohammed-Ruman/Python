# 16. Write a Python program to find the highest 3 values in a dictionary.

dic1={'z': 1, 'b': 2, 'c': 3, 'd': 4, 'w': 5, 'x': 6, 'y': 7, 'a': 8}

desc_dic=dict(sorted(dic1.items(),key=lambda x:x[1], reverse=True))

c=0;

for key, value in desc_dic.items():
    if(c==3):
        break
    print(f"Key:{key} and Value:{value}")
    c+=1