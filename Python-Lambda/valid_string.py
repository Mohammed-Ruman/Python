# 8) Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda. 
# Minimum length : 10 input string: PaceWisd0m o/p: valid string 

check_string= lambda x : any(char.isupper() for char in x ) and any(char.islower() for char in x) and any(char.isdigit() for char in x) and len(x)>=10

res="valid string " if check_string("String25103") is True else "Invalid String"

print(res)