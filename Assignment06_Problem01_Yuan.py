#Assignment06 - Problem Geometric Shapes Calculation

#Design a base class called Shape with methods area() and perimeter() which will be overridden by
#derived classes Circle, Rectangle, and Triangle. Each subclass should have attributes specific to the
#details required to calculate the area and perimeter. Create a list of shapes and iterate over it, printing out
#the area and perimeter of each shape, demonstrating polymorphism
import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a = math.pi*self.radius**2
        print("Circle area = " + str(a))

    def perimeter(self):
        p = math.pi*2*self.radius
        print("Circle perimeter = " + str(p))

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        a = self.length*self.width
        print("Rectangle area = " + str(a))

    def perimeter(self):
        p = 2*(self.length + self.width)
        print("Rectangle perimeter = " + str(p))

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    #Heron's formula
    def area(self):
        s = (self.side1 + self.side2 + self.side3)/2
        a = math.sqrt(s*(s - self.side1)*(s - self.side2)*(s - self.side3))
        print("Triangle area = " + str(a))

    def perimeter(self):
        p = self.side1 + self.side2 + self.side3
        print("Triangle perimeter = " + str(p))

#--------------------------------------------------
def main():
    #list of shapes
    shapes = [
        Circle(2),
        Circle(7),
        Rectangle(1, 2),
        Rectangle(7, 8),
        Triangle(1, 2, 3),
        Triangle(7, 8, 9),
    ]
    #iteratre
    for shape in shapes:
        shape.area()
        shape.perimeter()

#--------------------------------------------------------
main()