# 10) Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings. 
original_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

sorted_list = sorted(original_list, key=lambda x: (isinstance(x, str), x))

print(sorted_list)


