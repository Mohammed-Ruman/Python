# 18. Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False
import sys

def main():

    list1=[{},{},{}]
    list2=[{1,2},{},{}]

    for list in list2:
        flag=check_empty(list)
        if flag==False:
            print(False)
            sys.exit()
            break
    print(True)

def check_empty(dic):
    if(len(dic)==0):
        return True
    else:
        return False
main()
