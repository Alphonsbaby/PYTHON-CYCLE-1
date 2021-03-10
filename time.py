# Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to
#find sum of 2 time.
class times:
     def __init__(self,h,m,s):
       self.h=h
       self.m=m
       self.s=s
     def __add__(self, other):
       return self.h + other.h, self.m + other.m, self.s + other.s
v1 = times(2,10,3)
v2 = times(5,2,1)
v3 = v1+v2
print(v3)

