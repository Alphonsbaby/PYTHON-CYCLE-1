 #Create a class Rectangle with private attributes length and width. Overload ‘<’  operator  to
#compare the area of 2 rectangles.
class Rectangle():
    def __init__(self, l, w):
        self.__length = l
        self.__width  = w

    def area(self):
        return self.__length*self.__width

    def __lt__(self):
        if (rec1 < rec2):
            print("Area of Rectangle 1 is less than Rectangle 2")
        else:
            print("Area of Rectangle 2 is greater than Rectangle 1")

print("Rectangle 1")
a=int(input("enter the length:"))
b= int(input("enter the breadth:"))
obj=Rectangle(a,b)

print("Area 1 = ",obj.area())

print("Rectangle 2")
a=int(input("enter the length:"))
b= int(input("enter the breadth:"))
ob=Rectangle(a,b)
print("Area 2= ",ob.area())

#compairing

rec1 = obj.area()
rec2 = ob.area()
obje=Rectangle(rec1,rec2)
obje.__lt__()
