# 15. Write a Python program to count repeated characters in a string.

def main():
    strng=get_input()
    res=dict()

    for chr in strng:
        if chr in res:
            res[chr]=res.get(chr)+1
        else:
            res[chr]=1

    print(res)

    for chr in res:
        if res.get(chr)==1:
            pass
        else:
            print(chr, res.get(chr))
    
    

def get_input():
    return input("Enter the String? ")
    

main() 