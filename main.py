#_____  sources  _____
#https://www.code4example.com/python/python-program-to-calculate-area-and-perimeter-of-rectangle/
#https://www.code4example.com/python/python-program-to-calculate-area-and-perimeter-of-triangle/

# ____________   IMPORTS ________________
import math #import to be able to use pi in calculations
from main import * #import to be able to use pi and acos in calculations
from math import sin, radians #import to be able to use sin and radians in Triangle calculations
import tkinter as tk
from tkinter import messagebox #importing message box to display errors
from tkinter import ttk
from trianglecode import * #importing 'def trianglecode():'
from rectanglecode import * #importing 'def rectanglecode():'
from parallelogramcode import * #importing 'def parallelogramcode():'
from circlecode import * #importing 'def circlecode():'


# ____________   FUNCTIONS ________________
def clearBox(self):
    self.txt1.delete("1.0", "end")

def opentriwindow():
  trianglecode() #runs code that opens new window that has triagnle length inputs and calculate area and perimeter button as well as calculated and displayed area and perimeter
  
def openrectwindow():
  rectanglecode() #runs code that opens new window that has rectangle length inputs and calculate area and perimeter button as well as calculated and displayed area and perimeter
  global window

def openparallelwindow():
  parallelogramcode() #runs code that opens new window that has parallelogram length inputs and calculate area and perimeter button as well as calculated and displayed area and perimeter

def opencircwindow(): 
  circlecode() #runs code that opens new window that has circle radius input and calculate area and circumference button as well as calculated and displayed area and perimeter

# ____________   MAIN  ________________
  # Creating a custom window
window = tk.Tk()
window.geometry("500x285")
window.config(bg="#858585")
window.resizable(width=False,height=False)
window.title('Area and Perimeter Calculator')

# Labels for Heading and Subheadng of GUI
lb_heading = tk.Label(window,text="The Area and Perimeter Calculator",font=("Arial", 20),fg="black",bg="#858585")
lb_subheading = tk.Label(window,font=("Arial",11),text="Click on What Shape you want to find the Area and perimeter of..",fg="black",bg="#858585")

# Button to Open Triangle window
btn_calculate_triangle = tk.Button(window,text="Triangle",font=("Arial",13), command=lambda:[opentriwindow()])

# Button to Open Rectangle window
btn_calculate_rectangle = tk.Button(window,text="Rectangle / Square",font=("Arial",13), command=lambda:[openrectwindow()])

# Button to Open Parallelogram window
btn_calculate_parallelogram = tk.Button(window,text="Parallelogram",font=("Arial",13),command=lambda:[openparallelwindow()])

# Button to Open Circle window
btn_calculate_circle = tk.Button(window,text="Circle",font=("Arial",13),command=lambda:[opencircwindow()])

# Button to exit application
btn_exit = tk.Button(window,text="Exit Application",font=("Arial",13),command=exit)

# Placing the elements on the screen with co-ords
lb_heading.place(x=15,y=5)
lb_subheading.place(x=5,y=55)
btn_calculate_triangle.place(x=50,y=105)
btn_calculate_rectangle.place(x=140,y=170)
btn_calculate_parallelogram.place(x=305,y=105)
btn_calculate_circle.place(x=190,y=105)
btn_exit.place(x=155,y=230)