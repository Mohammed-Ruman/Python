# 13. Write a Python program to check whether a string starts with specified characters.

def main():
    in_str, in_chr=get_input()

    if(in_str[0]==in_chr):
        print(True)
    else:
        print(False)

def get_input():
    strng= input("Enter the String? ")
    chcr= input("Enter the Character? ")
    return strng,chcr

main()