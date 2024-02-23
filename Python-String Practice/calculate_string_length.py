# 1. Write a Python program to calculate the length of a string.

def main():
    input_string=input("Enter the String to Calculate the Length? ")

    print("String length is:",get_length(input_string))

def get_length(string):
    return len(string)

main()