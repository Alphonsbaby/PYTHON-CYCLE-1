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


a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
obj = Rectangle(a, b)
print("Area of rectangle:", obj.area())
print("perimeter of rectangle:", obj.peri())


