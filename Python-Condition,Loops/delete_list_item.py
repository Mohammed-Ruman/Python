# 16. Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element,
# if found. Iterate over list using for loop.

def main():
    get_lst=create_list()

    search_ele=int(input("Enter the Element to delete "))

    print(f"List before {get_lst}")

    if search_ele in get_lst:
        get_lst.remove(search_ele)

    print(f"List After {get_lst}")



def create_list():
    lst=list()
    size=int(input("Size of list? "))

    for i in range(0,size):
        ele=int(input("Enter the list element? "))
        lst.append(ele)
    
    return lst

main()