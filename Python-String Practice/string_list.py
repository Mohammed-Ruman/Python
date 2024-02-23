# 17. Write a Python program to convert a string in a list.

def main():
    strng=get_input()
    res=list()

    for ch in strng:
        res.append(ch)

    print(res)
def get_input():
    in_str= input("Enter the String? ")
    return in_str

main() 