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
  def find_circum(r):
    d=r+r #calculates diameter
    p=math.pi*d #calculates circumference using pi and the diameter
    circumference=round(p, 3) #rounds circumference to 3DP
    return circumference

  def find_area(r):
    a=math.pi*r*r #calculates area using pi and the radius squared
    area = round(a, 3) #round area to 3DP
    return area

  def display_area(area):
    tbox_area.config(state='normal')

    #area calculated is inserted into the text box after clearing the previous info in the textbox. 
    tbox_area.delete('1.0', tk.END)
    tbox_area.insert(tk.END,area)
    tbox_area.config(state='disabled')
  
  def display_circum(circumference):
    tbox_circum.config(state='normal')
    #area calculated is inserted into the text box after clearing the previous info in the textbox. 
    tbox_circum.delete('1.0', tk.END)
    tbox_circum.insert(tk.END,circumference)
    tbox_circum.config(state='disabled')

  def validation(): 
    # gets the radius entry
    r = radius.get()
    
    msg = '' #makes the message box 'clear'
    
    if len(r) == 0: #checks if the number of characters in the input boxes = 0
      msg = 'Please Do Not leave any Input Boxes Empty' #Inputs the error message that pops up
      calc_area = ' ' #clears the Calc Area box
      display_area(calc_area) #clears calc area box by printing the cleared the Calc Area box
      calc_circum = ' ' #clears the Calc circumference box
      display_circum(calc_circum) #clears calc circum box by printing the cleared the Calc Circumference box
      
    else:
      try:
        if any(ch.isdigit() for ch in r) == False:
          msg = 'Side length must be a NUMBER, EG: 5, not "five" or "fifth"' #Inputs the error message that pops up
          calc_area = ' ' #clears the Calc Area box
          display_area(calc_area) #clears calc area box by printing the cleared the Calc Area box
          calc_circum = ' ' #clears the Calc circumference box
          display_circum(calc_circum) #clears calc circum box by printing the cleared the Calc Circumference box
          
        else:
          #converts radius input to float
          r = float(r)

          if r <= 0:
            msg = 'Please Do Not Input a Negative length' #Inputs the error message that pops up
            calc_area = ' ' #clears the Calc Area box
            display_area(calc_area) #clears calc area box by printing the cleared the Calc Area box
            calc_circum = ' ' #clears the Calc circumference box
            display_circum(calc_circum) #clears calc circum box by printing the cleared the Calc Circumference box
            
          else:
            calc_area= find_area(r) #calculates area using the radius
            display_area(calc_area) #displays calculated area
            calc_circum = find_circum(r) #calculates circumference using the radius
            display_circum(calc_circum) #displays calculated circumference
      except Exception as ep:
        messagebox.showerror('error', ep) #prints and error message to tell the user and error happened according to the syntax error

    
    if msg != '':
      messagebox.showinfo('message', msg) #program checks if message box is clear and if not prints message box with new data
      
  # Creating a custom window
  window = tk.Tk()
  window.geometry("500x380")
  window.config(bg="#858585")
  window.resizable(width=False,height=False)
  window.title('Circle')
  
  # Labels for Heading and Subheadng of GUI
  lb_heading = tk.Label(window,text="Circle Area and Circumference \n Calculator",font=("Arial", 20),fg="black",bg="#858585")
  lb_subheading = tk.Label(window,font=("Arial",11),text="Please input the side lengths of the Circle you want to find\nthe Area and Circumference of.." ,fg="black",bg="#858585")

  #labels for side length inputs and text boxes
  lb_radius = tk.Label(window,font=("Arial",11),text="Radius" ,fg="black",bg="#858585")
  lb_area = tk.Label(window,font=("Arial",13),text="Area Calculated:" ,fg="black",bg="#858585")
  lb_circum = tk.Label(window,font=("Arial",13),text="Circumference:" ,fg="black",bg="#858585")
  tbox_area=tk.Text(window,width=6,height=1,state="disabled",font=('Arial',24,"bold"))  
  tbox_circum=tk.Text(window,width=6,height=1,state="disabled",font=('Arial',24,"bold"))
    
   # Entry boxes for date, month and year
  radius = tk.Entry(window,width=15)
  
  # Button to Open Triangle window
  btn_calculate = tk.Button(window,text="Calculate Area\nand Circumference",font=("Arial",11), command=validation)

  # Button to exit application
  btn_exit = tk.Button(window,text="Return to\nShape Chooser",font=("Arial",13),command=window.destroy)
  
  # Placing the elements on the screen with co-ords
  lb_heading.place(x=76,y=5)
  lb_subheading.place(x=22,y=80)
  lb_radius.place(x=20,y=220)
  lb_area.place(x=290,y=130)
  lb_circum.place(x=290,y=220)
  tbox_area.place(x=290,y=165)
  tbox_circum.place(x=290,y=255)
  radius.place(x=120,y=220)
  btn_calculate.place(x=65,y=316)
  btn_exit.place(x=290,y=313)
  