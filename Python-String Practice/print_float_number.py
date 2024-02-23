# 14. Write a Python program to print the following floating numbers upto 2 decimal places.
# 3.1415926

def main():
    num=get_input()
    print(f"{num:0.2f}")

def get_input():
    return float(input("Enter the Float Number? "))
    

main() 