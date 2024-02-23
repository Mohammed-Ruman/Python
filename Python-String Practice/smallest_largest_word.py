
# 19. Write a Python program to find smallest and largest word in a given string.

def main():
    print(find_longest_smallest(get_list()))

def find_longest_smallest(words):
    max_size = 0
    min_size = float('inf')
    max_index = -1
    min_index = -1

    for i in range(0, len(words)):
        if len(words[i]) > max_size:
            max_size = len(words[i])
            max_index = i
        if len(words[i]) < min_size:
            min_size = len(words[i])
            min_index = i

    return "Largest Word: " + words[max_index] + " Smallest Word: " + words[min_index]

def get_list():
    input_string = input("Enter the words separated by space: ")
    return input_string.split()

main()
