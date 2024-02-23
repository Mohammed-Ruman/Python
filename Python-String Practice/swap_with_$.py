''' 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', 
except the first char itself.'''

def main():
    print(swap_with_dollar(get_input()))

def swap_with_dollar(input_str):
    # for i in range(1,len(input_str)):
    #     if(input_str[i]==input_str[0]):
    #         input_str[i]="$"
    # return input_str

    str1=input_str[0:1]
    str2=input_str[1:]

    res=str2.replace(str1.lower(),"$")
    

    return str1+res

def get_input():
    return input("Enter the String? ")
    

main()