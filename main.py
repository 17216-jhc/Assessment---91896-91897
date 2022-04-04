#_____  sources  _____
#https://www.code4example.com/python/python-program-to-calculate-area-and-perimeter-of-rectangle/
#https://www.code4example.com/python/python-program-to-calculate-area-and-perimeter-of-triangle/

# ____________   IMPORTS ________________
import math
from main import *
from math import sin, radians
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from trianglecode import *
from rectanglecode import *
from parallelogramcode import *
from circlecode import *


# ____________   FUNCTIONS ________________
def clear():
   print("\033[H\033[J", end="") #clears the Console

def clearBox(self):
    self.txt1.delete("1.0", "end")

def opentriwindow():
  trianglecode()
  
def openrectwindow():
  rectanglecode()

def openparallelwindow():
  parallelogramcode()

def opencircwindow():
  circlecode()

def display_calc_area():
  tbox_area.config(state='normal')

    #age calculated is inserted into the text box after clearing the previous info in the textbox. 
  tbox_area.delete('1.0', tk.END)
  tbox_area.insert(tk.END,age)
  tbox_area.config(state='disabled')
  
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
  elif what_shape == 4:
    clear() #clears the Console
    circle() #runs code to get user to input sides of the shape and calculates perimter and area of triangle 
  else:
    print("\n Sorry please enter a valid input \n")

def A(shape, final_area):
  print(f"Area of {shape} : ",round(final_area, 4)) #prints the Area of shape
  
def P(shape, final_perimeter):
  print(f"Perimeter of {shape} : ", round(final_perimeter, 4)) #Prints the perimter of shape


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
  if l < h:
    clear()
    print("Sorry, that Parallelograms is Impossible, make the Height input Less than the Length")
    parallel()
    
  else:
    print()
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


  A(shape_chosen, area) #prints area
  P(shape_chosen, perimeter) #prints Perimeter
  print()

# ____________   MAIN  ________________
  # Creating a custom window
window = tk.Tk()
window.geometry("500x230")
window.config(bg="#858585")
window.resizable(width=False,height=False)
window.title('Area and Perimeter Calculator')

# Labels for Heading and Subheadng of GUI
lb_heading = tk.Label(window,text="The Area and Perimeter Calculator",font=("Arial", 20),fg="black",bg="#858585")
lb_subheading = tk.Label(window,font=("Arial",11),text="Click on What Shape you want to find the Area and perimeter of..",fg="black",bg="#858585")

# Button to Open Triangle window
btn_calculate_triangle = tk.Button(window,text="Triangle",font=("Arial",13), command=lambda:[window.destroy(), opentriwindow()])

# Button to Open Rectangle window
btn_calculate_rectangle = tk.Button(window,text="Rectangle / Square",font=("Arial",13), command=lambda:[openrectwindow(), exit])

# Button to Open Parallelogram window
btn_calculate_parallelogram = tk.Button(window,text="Parallelogram",font=("Arial",13),command=lambda:[openparallelwindow(), exit])

# Button to Open Circle window
btn_calculate_circle = tk.Button(window,text="Circle",font=("Arial",13),command=lambda:[opencircwindow(), exit])

# Placing the elements on the screen with co-ords
lb_heading.place(x=15,y=5)
lb_subheading.place(x=5,y=55)
btn_calculate_triangle.place(x=50,y=105)
btn_calculate_rectangle.place(x=140,y=170)
btn_calculate_parallelogram.place(x=305,y=105)
btn_calculate_circle.place(x=190,y=105)