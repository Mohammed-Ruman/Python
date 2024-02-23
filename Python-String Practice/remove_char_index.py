# 9. Write a Python program to remove the nth index character from a nonempty string.

def main():
    input_str=input("Enter the String? ")
    index=int(input("Enter the index of character to remove? "))

    print(input_str[:index]+input_str[index+1:])

main()