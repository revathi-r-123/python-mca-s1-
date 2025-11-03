from graphics . rectangle import *
from graphics  .circle import *
from graphics .threeD_graphics.cuboid import *
from graphics .threeD_graphics.sphere import *
r=int(input("Enter radius:"))
l=int(input("Enter lenght:"))
b=int(input("Enter breadth:"))
h=int(input("Enter height:"))
print("\n____PERIMETER AND AREA________\n")
print("Perimeter of rectangle:",perimeter_rectangle(l,b))
print("Area of rectangle:",area_rectangle(l,b))
print("Circumference of circle:",circumference_circle(r))
print("Area of circle:",area_circle(r))
print("Perimeter of cuboid:",perimeter_cuboid(l,b,h))
print("Area of cuboid:",area_cuboid(l,b,h))
print("Circumference of sphere:",circumference_sphere(r))
print("Area of sphere:",area_sphere(r))
