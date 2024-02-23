# 11. Write a Python function to reverses a string if it's length is a multiple of 4. 

def main():
    input=get_input()

    if(len(input)%4==0):
        print(input[::-1])


def get_input():
    return input("Enter the String? ")
    

main()