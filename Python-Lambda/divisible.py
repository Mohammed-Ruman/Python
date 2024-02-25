# 6)  Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda 

Orginal_list= [19, 65, 57, 39, 152, 639, 121, 44, 90, 190] 

res=list()

div=lambda x: True if x%19==0 or x%13==0 else False

for list in Orginal_list:
    if(div(list)):
        res.append(list)

print(res)