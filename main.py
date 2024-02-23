def main():
    x=get_int()
    print("x is ",x)

def hello(to="world"):
    if(to>0):
        print("Positive Number", to)
    elif(to<0):
        print("Negative Number")
    else:
        print("Neutral Number")

def get_int():
    while True:
        try:
            return int(input("Whats X? "))
        except ValueError:
            print("X is not int")
       
        
        
main()
