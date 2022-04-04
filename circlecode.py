#_____ IMPORTS ______
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



#_____ DEFINITIONS _____
def clearBox(self):
    self.txt1.delete("1.0", "end")

def display_area(age):
    tbox_area.config(state='normal')
  
def display_area(age):
    tbox_perim.config(state='normal')
  
  # ____________   Circle WINDOW  ________________
def circlecode():
  # Creating a custom window
  window = tk.Tk()
  window.geometry("500x380")
  window.config(bg="#858585")
  window.resizable(width=False,height=False)
  window.title('Circle')
  
  # Labels for Heading and Subheadng of GUI
  lb_heading = tk.Label(window,text="Circle Area and Perimeter \n Calculator",font=("Arial", 20),fg="black",bg="#858585")
  lb_subheading = tk.Label(window,font=("Arial",11),text="Please input the side lengths of the Circle you want to find\nthe Area and Perimeter of.." ,fg="black",bg="#858585")

  lb_radius = tk.Label(window,font=("Arial",11),text="Radius Length" ,fg="black",bg="#858585")

  lb_area = tk.Label(window,font=("Arial",13),text="Area Calculated:" ,fg="black",bg="#858585")

  lb_perim = tk.Label(window,font=("Arial",13),text="Perimeter Calculated:" ,fg="black",bg="#858585")

  tbox_area=tk.Text(window,width=5,height=1,state="disabled",font=('Arial',24,"bold"))

  tbox_perim=tk.Text(window,width=5,height=1,state="disabled",font=('Arial',24,"bold"))
  
 # Entry boxes for date, month and year
  radius = tk.Entry(window,width=15)
  
  # Button to Open Circle window
  btn_calculate_Circle = tk.Button(window,text="Calculate Area and Perimeter",font=("Arial",11))

  # Button to exit application
  btn_exit = tk.Button(window,text="Return to\nShape Chooser",font=("Arial",13),command=window.destroy)
  
  # Placing the elements on the screen with co-ords
  lb_heading.place(x=55,y=5)
  lb_subheading.place(x=22,y=75)
  lb_radius.place(x=20,y=210)
  lb_area.place(x=290,y=130)
  lb_perim.place(x=290,y=220)
  tbox_area.place(x=290,y=165)
  tbox_perim.place(x=290,y=255)
  radius.place(x=140,y=210)
  btn_calculate_Circle.place(x=22,y=327)
  btn_exit.place(x=290,y=313)
  