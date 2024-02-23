# 18. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

def main():
    strng=get_input()

    print(strng.replace(",","."))

def get_input():
    in_str= input("Enter the String? ")
    return in_str

main() 