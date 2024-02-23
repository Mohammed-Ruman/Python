# 3. Write a Python program to get a string made of the first 2 and 
# the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string. 

def main():
    print(concat_string(get_input()))

def concat_string(input_str):
    if(len(input_str)<2):
        return "Empty String"
    return input_str[0:2]+input_str[-2:]

def get_input():
    return input("Enter the String? ")
    

main()