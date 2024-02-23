# 13. Take 10 integers from keyboard using loop and print their average value on the screen.
sum=0

for i in range(0,10):
    num=int(input("Enter the Number? "))
    sum += num

print(sum/10)