# 7. Write a Python program that counts the number of elements within a list that are greater than 30.

lst=[20,30,40,50,10,20]
count=0

for element in lst:
    if element > 30:
        count +=1
print(count)