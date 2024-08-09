p=input("Enter Principal:")
r=input("Enter Rate:")
t=input("Enter Time:")
simple_interest = (int(p) * int(r) * int(t))/int(100)
print("The simple interest is :", simple_interest)
#this is another programme about calculating area of a a circle
from math import pi
r=int(input("Enter the radius of a circle: "))
a=pi*r*r
print("This is the area of a circle ", a)
#you can also round up a value into decimal place you want
print("This is the area of a circle", round(a,2))