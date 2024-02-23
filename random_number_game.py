import random


def main():
    randomNum=random.randint(1,100)
    count=0
    while True:
        num=get_int("Guess the Number? ")

        if(num>randomNum):
            print("Your choosen Number is greater than Random Number")
            count += 1
        elif(num<randomNum):
            print("Your choosen Number is less than Random Number")
            count += 1
        else:
            print("Congratulation! You guessed it right", randomNum)
            print("Number of Guess= ", count)
            break
    

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Kindly Input a Number")

main()
        