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
    print()

def in_values(side):
  value=float(input(f"Enter {side}: "))
  return value

def A(shape, final_area):
  print(f"Area of {shape} : ",final_area)
  
def P(shape, final_perimeter):
  print(f"Perimeter of {shape} : ",final_perimeter)

def triangle():
  clear()
  shape_chosen = "Triangle"
  print(shape_chosen)
  b=in_values("Base")
  s1=in_values("Side 1")
  s2=in_values("Side 2")
  h=in_values("Height")
  area=0.5 * b * h
  perimeter=b+s1+s2
  print()
  
  A(shape_chosen, area)
  P(shape_chosen, perimeter)
  print()

def rectangle():
  clear()
  shape_chosen = "Rectangle"
  print(shape_chosen)
  l=in_values("Length")
  w=in_values("Width")
  area=l*w
  perimeter=2*(l+w)
  print()
  
  A(shape_chosen, area)
  P(shape_chosen, perimeter)
  print()
  
def parallel():
  clear()
  shape_chosen = "Parallelogram"
  print(shape_chosen)
  l=in_values("Length")
  w=in_values("Width")
  h=in_values("Height")
  area=h*w
  perimeter=2*(l+w)
  print()
  
  A(shape_chosen, area)
  P(shape_chosen, perimeter)
  print()

def circle():
  clear()
  shape_chosen = "Circle"
  print(shape_chosen)
  r=in_values("Radius")
  d=r+r
  area=math.pi*r*r
  perimeter=math.pi*d
  print()

  A(shape_chosen, area)
  P(shape_chosen, perimeter)
  print()

# ____________   MAIN  ________________
shapes = ["triangle", "Rectangle / Square", "Parallelogram", "Circle"]
keep_going = "yes"
while keep_going == "yes":
  

  try:
    
      
    print("Please select shape you want to use by typing in a number between 1 and 4")
    i = 1
    for x in shapes : 
      print(i,"=", x)
      i+= 1
    what_shape = int(input("Select: "))
  
    shape_chooser()
    
  except ValueError:
    print()
