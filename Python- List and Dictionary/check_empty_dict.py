# 14. Write a Python program to check a dictionary is empty or not. 

def main():
    dic1={'z': 1, 'b': 2, 'c': 3, 'd': 4, 'w': 5, 'x': 6, 'y': 7, 'a': 8}
    dic2={}

    check_empty(dic1)

    check_empty(dic2)

def check_empty(dic):
    if(len(dic)==0):
        print("Dictionary is Empty")
    else:
        print("Dictionary is not Empty")

main()