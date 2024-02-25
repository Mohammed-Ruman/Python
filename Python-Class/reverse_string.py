# 7) Write a Python class to reverse a string word by word. 
# Input string : 'hello .py' Expected Output : '.py hello' 

class Reverse():
    def __init__(self):
        pass

    def reverse_string(self, strng):
        strng_lst=strng.split()

        rev_strng= strng_lst[::-1]

        for st in rev_strng:
            print(st)


reverse=Reverse()

reverse.reverse_string("hello .py")

