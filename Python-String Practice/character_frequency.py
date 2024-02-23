
# 2. Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

def main():
    input_string= input("Enter the String? ")
    processed_string=input_string.replace(" ","")

    print("Character Frequency",calculate_frequency(processed_string))

def calculate_frequency(input_string):
    res=dict()

    for i in input_string:
        if i in res:
            res[i]=1+res[i]
        else:
            res[i]=1
    
    return res
            
main()
