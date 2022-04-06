#_____ IMPORTS ______
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from main import *



#_____ DEFINITIONS _____
def clearBox(self):
    self.txt1.delete("1.0", "end")
  
  # ____________   TRIANGLE WINDOW  ________________
def circlecode():
  def find_perim(r):
    d=r+r #calculate diameter
    p=math.pi*d #calculates perimeter using pi and the diameter
    perimeter=round(p, 3)
    return perimeter

  def find_area(r):
    a=math.pi*r*r #calculates area using pi and the radius squared
    area = round(a, 3)
    return area

  def display_area(area):
    tbox_area.config(state='normal')

    #area calculated is inserted into the text box after clearing the previous info in the textbox. 
    tbox_area.delete('1.0', tk.END)
    tbox_area.insert(tk.END,area)
    tbox_area.config(state='disabled')
  
  def display_perim(perimeter):
    tbox_perim.config(state='normal')
    #area calculated is inserted into the text box after clearing the previous info in the textbox. 
    tbox_perim.delete('1.0', tk.END)
    tbox_perim.insert(tk.END,perimeter)
    tbox_perim.config(state='disabled')

  def validation(): 
    # gets the three entries
    r = radius.get()
    
    msg = ''
    
    if len(r) == 0: #checks if the number of characters in the input boxes = 0
      msg = 'Please Do Not leave any Input Boxes Empty'
      calc_area = ' ' #clears the Calc Area box
      display_area(calc_area)
      calc_perim = ' ' #clears the Calc Perimeter box
      display_perim(calc_perim)
      
    else:
      try:
        if any(ch.isdigit() for ch in r) == False:
          msg = 'Side length must be a NUMBER, EG: 5, not "five" or "fifth"'
          calc_area = ' ' #clears the Calc Area box
          display_area(calc_area)
          calc_perim = ' ' #clears the Calc Perimeter box
          display_perim(calc_perim)
          
        else:
          r = float(r)

          if r <= 0:
            msg = 'Please Do Not Input a Negative length'
            calc_area = ' ' #clears the Calc Area box
            display_area(calc_area)
            calc_perim = ' ' #clears the Calc Perimeter box
            display_perim(calc_perim)
            
          else:
            calc_area= find_area(r)
            display_area(calc_area)
            calc_perim = find_perim(r)
            display_perim(calc_perim)
      except Exception as ep:
        messagebox.showerror('error', ep)
        print(ep)

    
    if msg != '':
      messagebox.showinfo('message', msg)
  # Creating a custom window
  window = tk.Tk()
  window.geometry("500x380")
  window.config(bg="#858585")
  window.resizable(width=False,height=False)
  window.title('Circle')
  
  # Labels for Heading and Subheadng of GUI
  lb_heading = tk.Label(window,text="Circle Area and Perimeter \n Calculator",font=("Arial", 20),fg="black",bg="#858585")
  lb_subheading = tk.Label(window,font=("Arial",11),text="Please input the side lengths of the Circle you want to find\nthe Area and Perimeter of.." ,fg="black",bg="#858585")

  lb_radius = tk.Label(window,font=("Arial",11),text="Radius" ,fg="black",bg="#858585")

  lb_area = tk.Label(window,font=("Arial",13),text="Area Calculated:" ,fg="black",bg="#858585")

  lb_perim = tk.Label(window,font=("Arial",13),text="Perimeter Calculated:" ,fg="black",bg="#858585")

  tbox_area=tk.Text(window,width=6,height=1,state="disabled",font=('Arial',24,"bold"))
  
  tbox_perim=tk.Text(window,width=6,height=1,state="disabled",font=('Arial',24,"bold"))
    
   # Entry boxes for date, month and year
  radius = tk.Entry(window,width=15)
  
  # Button to Open Triangle window
  btn_calculate = tk.Button(window,text="Calculate Area and Perimeter",font=("Arial",11), command=validation)

  # Button to exit application
  btn_exit = tk.Button(window,text="Return to\nShape Chooser",font=("Arial",13),command=window.destroy)
  
  # Placing the elements on the screen with co-ords
  lb_heading.place(x=76,y=5)
  lb_subheading.place(x=22,y=80)
  lb_radius.place(x=20,y=220)
  lb_area.place(x=290,y=130)
  lb_perim.place(x=290,y=220)
  tbox_area.place(x=290,y=165)
  tbox_perim.place(x=290,y=255)
  radius.place(x=120,y=220)
  btn_calculate.place(x=22,y=327)
  btn_exit.place(x=290,y=313)
  