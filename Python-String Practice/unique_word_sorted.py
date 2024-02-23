# 10. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white

def main():
    list=get_list()

    res_set=set(list)

    res=sorted(res_set)

    for re in res:
        print(re, end=",")
    
    print()


def get_list():
    input_string=input("Enter the words seperated by comma: ")
    in_str=input_string.replace(" ","")
    return in_str.split(",")

    

main()