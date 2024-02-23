# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing' 
# Sample String : 'string'
# Expected Result : 'stringly'

def main():
    print(add_ing(get_input()))

def add_ing(input_string):
    if(len(input_string)<3):
        return input_string
    elif(input_string[-3:]=="ing"):
        return input_string+"ly"
    else:
        return input_string+"ing"


def get_input():
    return input("Enter the String? ")
    

main()