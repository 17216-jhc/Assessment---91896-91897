#_____ IMPORTS ______
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from main import *



#_____ DEFINITIONS _____
def clearBox(self):
    self.txt1.delete("1.0", "end")
  
  # ____________   TRIANGLE WINDOW  ________________
def rectanglecode():
  def find_perim(l, w):
    p= 2*w + 2*l#calculates perimeter using base, length of side 1 and length of side 2
    perimeter=round(p, 3)
    return perimeter

  def find_area(l, w):
    a=l * w #calculates Area using base, height then halving
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
    l = length.get()
    w = width.get()
    
    msg = ''
    
    if len(l) == 0 or len (w) == 0: #checks if the number of characters in the input boxes = 0
      msg = 'Please Do Not leave any Input Boxes Empty'
      calc_area = ' ' #clears the Calc Area box
      display_area(calc_area)
      calc_perim = ' ' #clears the Calc Perimeter box
      display_perim(calc_perim)
      
    else:
      try:
        if any(ch.isdigit() for ch in l) == False or any(ch.isdigit() for ch in w) == False:
          msg = 'Side length must be a NUMBER, EG: 5, not "five" or "fifth"'
          calc_area = ' ' #clears the Calc Area box
          display_area(calc_area)
          calc_perim = ' ' #clears the Calc Perimeter box
          display_perim(calc_perim)
          
        else:
          l = float(l)
          w = float(w)

          if l <= 0 or w <= 0:
            msg = 'Please Do Not Input a Negative length'
            calc_area = ' ' #clears the Calc Area box
            display_area(calc_area)
            calc_perim = ' ' #clears the Calc Perimeter box
            display_perim(calc_perim)
            
          else:
            calc_area= find_area(l, w)
            display_area(calc_area)
            calc_perim = find_perim(l, w)
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
  window.title('Triangle')
  
  # Labels for Heading and Subheadng of GUI
  lb_heading = tk.Label(window,text="Triangle Area and Perimeter \n Calculator",font=("Arial", 20),fg="black",bg="#858585")
  lb_subheading = tk.Label(window,font=("Arial",11),text="Please input the side lengths of the Rectangle / Square you want to find\nthe Area and Perimeter of.." ,fg="black",bg="#858585")

  lb_length = tk.Label(window,font=("Arial",11),text="Length" ,fg="black",bg="#858585")

  lb_width = tk.Label(window,font=("Arial",11),text="Width" ,fg="black",bg="#858585")

  lb_area = tk.Label(window,font=("Arial",13),text="Area Calculated:" ,fg="black",bg="#858585")

  lb_perim = tk.Label(window,font=("Arial",13),text="Perimeter Calculated:" ,fg="black",bg="#858585")

  tbox_area=tk.Text(window,width=6,height=1,state="disabled",font=('Arial',24,"bold"))
  
  tbox_perim=tk.Text(window,width=6,height=1,state="disabled",font=('Arial',24,"bold"))
    
   # Entry boxes for date, month and year
  length = tk.Entry(window,width=15)
  
  width = tk.Entry(window,width=15)
  
  # Button to Open Triangle window
  btn_calculate = tk.Button(window,text="Calculate Area and Perimeter",font=("Arial",11), command=validation)

  # Button to exit application
  btn_exit = tk.Button(window,text="Return to\nShape Chooser",font=("Arial",13),command=window.destroy)
  
  # Placing the elements on the screen with co-ords
  lb_heading.place(x=55,y=5)
  lb_subheading.place(x=22,y=80)
  lb_width.place(x=20,y=195)
  lb_length.place(x=20,y=245)
  lb_area.place(x=290,y=130)
  lb_perim.place(x=290,y=220)
  tbox_area.place(x=290,y=165)
  tbox_perim.place(x=290,y=255)
  length.place(x=140,y=195)
  width.place(x=140,y=245)
  btn_calculate.place(x=22,y=327)
  btn_exit.place(x=290,y=313)
  