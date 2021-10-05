import math
from turtle import circle
from typing import TYPE_CHECKING
a = float(input("nhap a= "))
b = float(input("nhap b= "))
c = float(input("nhap c= "))
delta = b**2 - 4*a*c
x1 = (-b+ math.sqrt(delta))/(2*a)
x2 = (-b- math.sqrt(delta))/(2*a)
print("nghiem cua phuong trinh la: x1 =", x1)
print("nghiem cua phuong trinh la: x2 =", x2)