# 4. Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with two equal sides.
# Expected Output:
# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Scalene triangle 

def main():
   
    x,y,z=get_sides()

    if x==y==z:
        print("Equilateral Traingle")
    elif x == y or y == z or z == x:
        print("Isosceles Traingle")
    else:
        print("Scalene Traingle")


def get_sides():
   x= input("Enter X: ")
   y= input("Enter Y: ")
   z= input("Enter Z: ")
   return x,y,z

main()