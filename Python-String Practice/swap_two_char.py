# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def main():
    print(swap_char(get_input()))


def swap_char(input_string):
    list_string=input_string.split()

    str1=list_string[0]
    str2=list_string[1]
    
    temp1=str2[0:2]+str1[-1:]

    temp2=str1[0:2]+str2[-1:]

    return (temp1,temp2)



def get_input():
    return input("Enter the String? ")
    

main()