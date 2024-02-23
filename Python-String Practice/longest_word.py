# 8. Write a Python function that takes a list of words and returns the length of the longest one. 

def main():
    print(find_longest(get_list()))

def find_longest(words):
    max_size=0
    index=-1

    for i in range(0,len(words)):
        if len(words[i])>max_size:
            max_size=len(words[i])
            index=i
    return words[index]

def get_list():
    input_string=input("Enter the words seperated by space: ")

    return input_string.split()

    

main()