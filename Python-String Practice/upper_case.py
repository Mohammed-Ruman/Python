# 12. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def main():
    strng=get_input()
    c=0

    for chr in strng[:5]:
        if(chr.isupper()):
            c +=1
    
    if(c>=2):
        print(strng.upper())
    
    else:
        print(strng)

def get_input():
    return input("Enter the String? ")
    

main()