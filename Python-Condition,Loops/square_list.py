# 20.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.

in_lst=[2,5,6,7,8,9]

square=list()

for intg in in_lst:
    square.append(intg*intg)

print(square)