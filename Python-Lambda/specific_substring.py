
# 9) Write a Python program to find the elements of a given list of strings that contain specific substring using lambda. 

original_list = ['red', 'black', 'white', 'green', 'orange']
substring1 = 'ack'
substring2 = 'abc'

result1 = list(filter(lambda x: substring1 in x, original_list))
result2 = list(filter(lambda x: substring2 in x, original_list))

print(f"Elements of the said list that contain specific substring '{substring1}': {result1}")
print(f"Elements of the said list that contain specific substring '{substring2}': {result2}")
