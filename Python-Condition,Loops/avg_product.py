# 15. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

prod=1
c=0
sum=0
while(True):
    in_str=input("Enter the Number? or Press q to quit ")

    if(in_str=="q"):
        print(f"Product={prod} Average={sum/c}")
        break
    prod *= int(in_str)
    sum += int(in_str)
    c +=1