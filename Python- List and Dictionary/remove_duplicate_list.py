
# 19. Write a Python program to remove duplicates from a list of lists.
def remove_duplicates(list_of_lists):
    # Convert inner lists to tuples
    tuples = [tuple(lst) for lst in list_of_lists]
    
    # Remove duplicates by converting to set
    unique_tuples = set(tuples)
    
    # Convert back to list of lists
    unique_lists = [list(t) for t in unique_tuples]
    
    return unique_lists


list_of_lists = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]


new_list = remove_duplicates(list_of_lists)

print("New List:", new_list)


