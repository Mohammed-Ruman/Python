# 9) Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle. 

class Circle:
    def __init__(self,radius) :
        self._radius=radius

    def compute_area(self):
        print(f"Area is : {3.142*self._radius*self._radius}")

    def compute_perimeter(self):
        print(f"Perimeter is : {2*3.142*self._radius}")

circle=Circle(2)

circle.compute_area()
circle.compute_perimeter()