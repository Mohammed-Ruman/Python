# 14. Print multiplication table of 24, 50 and 29 using loop.

def main():
     table(24)
     print()
     table(50)
     print()
     table(29)


def table(num):
     for i in range(1,11):
          print(f"{num} * {i} = {num*i}")

main()