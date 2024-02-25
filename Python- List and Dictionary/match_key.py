
# 17. Write a Python program to match key values in two dictionaries.
dic1= {'key1': 1, 'key2': 3, 'key3': 2}
dic2={'key1': 1, 'key2': 2}

for key,value in dic1.items():
    if key in dic2 and dic2[key]==value:
        print("Key is Present in both Dictionary")
    else:
        print("Key doesnot present in both Dictionary")

