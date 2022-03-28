#_____  sources  _____
#https://www.code4example.com/python/python-program-to-calculate-area-and-perimeter-of-rectangle/
#https://www.code4example.com/python/python-program-to-calculate-area-and-perimeter-of-triangle/

# ____________   IMPORTS ________________
import math

# ____________   FUNCTIONS ________________
def clear():
   print("\033[H\033[J", end="") #clears the Console

def shape_chooser():
  if what_shape == 1:
    clear() #clears the Console
    triangle() #runs code to get user to input sides of the shape and calculates perimter and area of triangle 
  elif what_shape == 2:
    clear() #clears the Console
    rectangle() #runs code to get user to input sides of the shape and calculates perimter and area of triangle
  elif what_shape == 3:
    clear() #clears the Console
    parallel() #runs code to get user to input sides of the shape and calculates perimter and area of triangle 
    clear() #clears the Console
  elif what_shape == 4:
    clear() #clears the Console
    circle() #runs code to get user to input sides of the shape and calculates perimter and area of triangle 
  else:
    print()
    print("Sorry please enter a valid input #1")
    print()

def in_values(side):
  keep_going_2 = "yes"
  keep_going_3 = "yes"
  while keep_going_2 == "yes":
    try:
      value=float(input(f"Enter {side}: "))
      while keep_going_3 == "yes":
        if value <=0:
          while True:
            print("Please enter a positive value")
            value=float(input(f"Enter {side}: "))
            if value > 0:
              break     
        else:
          return value
    except ValueError:
      print("Please enter a Number")

def A(shape, final_area):
  print(f"Area of {shape} : ",final_area) #prints the Area of shape
  
def P(shape, final_perimeter):
  print(f"Perimeter of {shape} : ",final_perimeter) #Prints the perimter of shape

    
def triangle(): #def for finding the area of perimeter and area of a Triangle
  shape_chosen = "Triangle"
  print(shape_chosen) #prints what shape they are finding at the top
  b=in_values("Base") #asks user the Base of the shape and gets an input
  s1=in_values("Side 1") #asks user the length of side 1 of the shape and gets an input
  s2=in_values("Side 2") #asks user the length of side 2 of the shape and gets an input
  h=in_values("Height") #asks user the height of the shape and gets an input
  if s1 + s2 < b or b + s1 < s2 or b + s2 < s1:
    clear()
    print("Sorry, that Triangle is Impossible, please input a possible triangle")
    triangle()
  else:
    return
  area=0.5 * b * h #calculates Area using base, height then halving
  perimeter=b+s1+s2 #calculates perimeter using base, length of side 1 and length of side 2
  print()
  
  A(shape_chosen, area) #prints area
  P(shape_chosen, perimeter) #prints Perimeter
  print()

def rectangle(): #def for finding the area of perimeter and area of a rectangle
  shape_chosen = "Rectangle"
  print(shape_chosen) #prints what shape they are finding at the top
  l=in_values("Length") #asks user the length of the shape and gets an input
  w=in_values("Width")  #asks user the width of the shape and gets an input
  area=l*w #calculates Area using length and width
  perimeter=2*(l+w) #calculates perimeter using length and width
  print()
  
  A(shape_chosen, area) #prints area
  P(shape_chosen, perimeter) #prints Perimeter
  print()
  
def parallel(): #def for finding the area of perimeter and area of a paralleogram
  shape_chosen = "Parallelogram"
  print(shape_chosen) #prints what shape they are finding at the top
  l=in_values("Length")  #asks user the length of the shape and gets an input
  w=in_values("Width") #asks user the width of the shape and gets an input
  h=in_values("Height") #asks user the height of the shape and gets an input
  area=h*w #calculates Area using height and width
  perimeter=2*(l+w) #calculates perimeter using length and width
  print()
  
  A(shape_chosen, area) #prints area
  P(shape_chosen, perimeter) #prints Perimeter
  print()

def circle(): #def for finding the area of perimeter and area of a circle
  shape_chosen = "Circle"
  print(shape_chosen) #prints what shape they are finding at the top
  r=in_values("Radius") #asks user the radius of the shape and gets an input
  d=r+r
  area=math.pi*r*r #calculates area using pi and the radius squared
  perimeter=math.pi*d #calculates perimeter using pi and the diameter
  print()

  A(shape_chosen, area) #prints area
  P(shape_chosen, perimeter) #prints Perimeter
  print()

# ____________   MAIN  ________________
shapes = ["triangle", "Rectangle / Square", "Parallelogram", "Circle"] #list of each shape they can calculate are and perimter of
keep_going = "yes"

while keep_going == "yes": #loops main code to stop invalid inputs
  try: 
    print("Please select shape you want to use by typing in a whole number between 1 and 4")
    i = 1
    for x in shapes : 
      print(i,"=", x) #prints what number each shape correlates to
      i+= 1
    what_shape = int(input("Select: ")) #asks the user what shape they want to use
    shape_chooser() #runs code to run what formulas are used and sides are inputted
    
  except ValueError:
    print()
    print("Sorry please enter a valid input #2")
    print()
