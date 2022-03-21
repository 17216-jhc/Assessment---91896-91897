#_____  sources  _____
#https://www.code4example.com/python/python-program-to-calculate-area-and-perimeter-of-rectangle/
#https://www.code4example.com/python/python-program-to-calculate-area-and-perimeter-of-triangle/

# ____________   IMPORTS ________________
import math
# ____________   FUNCTIONS ________________
def clear():
   print("\033[H\033[J", end="")

def shape_chooser():
  if what_shape == 1:
    triangle()
  elif what_shape == 2:
    rectangle()
  elif what_shape == 3:
    parallel()
  elif what_shape == 4:
    circle()
  else:
    print("Incorrect Input, please use, 1, 2, 3 or 4")
    
def triangle():
  clear()
  print("Triangle")
  b=int(input("Enter Base : "))
  s1=int(input("Enter Side 1: "))
  s2=int(input("Enter Side 2: "))
  h=int(input("Enter Height: "))
  area=0.5 * b * h
  perimeter=b+s1+s2
  print()
  
  print("Area of Triangle : ",area)
  print("Perimeter of Rectangle : ",perimeter)

def rectangle():
  clear()
  print("Rectangle")
  l=int(input("Enter Length: "))
  w=int(input("Enter Width: "))
  area=l*w
  perimeter=2*(l+w)
  print()
  
  print("Area of Rectangle : ",area)
  print("Perimeter of Rectangle : ",perimeter)
  
def parallel():
  clear()
  print("parallelogram")
  l=int(input("Enter Length: "))
  w=int(input("Enter Width: "))
  h=int(input("Enter Height: "))
  area=h*w
  perimeter=2*(l+w)
  print()
  
  print("Area of Parallelogram : ",area)
  print("Perimeter of Parallelogram : ",perimeter)

def circle():
  clear()
  print("Circle")
  r=int(input("Enter Radius: "))
  d=r+r
  area=math.pi*r*r
  perimeter=math.pi*d
  print()
  
  print("Area of Circle : ",area)
  print("Perimeter of Circle : ",perimeter)

# ____________   MAIN  ________________
print("Please select shape you want to use by typing in a number between 1 and 4")
print("1 = Triangle")
print("2 = Rectangle / Square")
print("3 = Parallelogram")
print("4 = Circle")
what_shape = int(input("Select: "))
shape_chooser()








 


