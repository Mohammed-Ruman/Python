# 19. From a list containing ints, strings and floats, make three lists to store them separately

lst=[1,"one",1.01,2,"two",2.02]
ints=list()
strings=list()
floats=list()

for l in lst:
    if type(l) == int:
        ints.append(l)
    elif type(l) == str:
        strings.append(l)
    else:
        floats.append(l)

print(ints)
print(strings)
print(floats)