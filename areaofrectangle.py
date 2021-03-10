#1.  Create  Rectangle  class  with  attributes  length  and  breadth  and  methods  to  find  area  and
#perimeter. Compare two Rectangle objects by their area.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    def peri(self):
        return 2*(self.length + self.breadth)

print("rectangle 1")
a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
obj = Rectangle(a, b)
print("Area of rectangle 1:", obj.area())
print("perimeter of rectangle 1:", obj.peri())


print("Rectangle 2")
a=int(input("enter the length:"))
b= int(input("enter the breadth:"))
ob=Rectangle(a,b)


print("Area 2= ",ob.area())
print("Perimeter=",ob.peri())

if  obj.area() == ob.area():
    print("The 2 rectangle have same area")
else:
    print("not equal")

