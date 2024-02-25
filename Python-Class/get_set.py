# 8) Write a python class which has 2 methods get_string and print_string. get_string takes a string from the user
# and print_string prints the string in reverse order 

class Reverse():

    def get_string(self,strng):
        self._strng=strng

    def print_string(self,strng):
        rev_strng=strng[::-1]
        for char in rev_strng:
            print(char,end=" ")
        

        
reverse=Reverse()

reverse.print_string("hello")