# 16. Write a Python program to print the index of the character in a string.

def main():
    strng, chr=get_input()

    print(strng.find(chr))

def get_input():
    in_str= input("Enter the String? ")
    in_chr= input("Enter the Character? ")
    return in_str, in_chr

main() 