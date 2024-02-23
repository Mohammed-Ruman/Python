# 5. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish

c=0
sum=0
while(True):
    num=int(input("Enter the Number: "))
    if(num==0):
        avg=sum/c
        print(f"Sum = {sum} and Average ={avg}")
        break
    sum += num
    c += 1