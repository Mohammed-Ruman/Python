# 17. Using range(1,101), make three list, 
# one containing all even numbers
# one containing all odd numbers 
# One containing only prime numbers..

even=list()
odd=list()
prime=list()

for i in range(1,101):
    if i!=1 and i%2!=0:
        prime.append(i)
    if i==1:
        prime.append(i)

    if i%2==0:
        even.append(i)
    if i%2!=0:
        odd.append(i)

print(even)
print(odd)
print(prime)
    
