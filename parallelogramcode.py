#_____ IMPORTS ______
from main import * #importing imports from main



#_____ DEFINITIONS _____
def find_perim(l, w):
  p= 2*w + 2*l#calculates perimeter using width and length
  perimeter=round(p, 2) #rounds calculated perimeter to 2DP
  return perimeter

def find_area(w, h):
  a=h * w #calculates Area using height and width
  area = round(a, 2) #rounds calculated area to 2DP
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
  h = height.get()
  
  msg = '' #makes the message box 'clear'
  
  if len(l) == 0 or len (w) == 0: #checks if the number of characters in the input boxes = 0
    msg = 'Please Do Not leave any Input Boxes Empty' #Inputs the error message that pops up
    calc_area = ' ' #clears the Calc Area box
    display_area(calc_area) #clears calc area box by printing the cleared the Calc Area box
    calc_perim = ' ' #clears the Calc Perimeter box
    display_perim(calc_perim) #clears calc perim box by printing the cleared the Calc Perimeter box
    
  else:
    try:
      if any(ch.isdigit() for ch in l) == False or any(ch.isdigit() for ch in w) == False: #checks if the sides inputted by user contain letters or symbols (str)
        msg = 'Side length must be a NUMBER, EG: 5, not "five" or "fifth"' #Inputs the error message that pops up
        calc_area = ' ' #clears the Calc Area box
        display_area(calc_area) #clears calc area box by printing the cleared the Calc Area box
        calc_perim = ' ' #clears the Calc Perimeter box
        display_perim(calc_perim) #clears calc perim box by printing the cleared the Calc Perimeter box
        
      else:
        #converting side lengths to float
        l = float(l)
        w = float(w)
        h = float(h)

        if l <= 0 or w <= 0:
          msg = 'Please Do Not Input a Negative length' #Inputs the error message that pops up
          calc_area = ' ' #clears the Calc Area box
          display_area(calc_area) #clears calc area box by printing the cleared the Calc Area box
          calc_perim = ' ' #clears the Calc Perimeter box
          display_perim(calc_perim) #clears calc perim box by printing the cleared the Calc Perimeter box
          
        else:
          calc_area= find_area(w, h) #calculates area using height and width
          display_area(calc_area) #displays calculated area
          calc_perim = find_perim(l, w) #calculates perimeter using length and width
          display_perim(calc_perim) #displays calculated perimeter
    except Exception as ep:
      messagebox.showerror('error', ep) #prints and error message to tell the user and error happened according to the syntax error

  
  if msg != '':
    messagebox.showinfo('message', msg)  #program checks if message box is clear and if not prints message box with new data
      
  # ____________   TRIANGLE WINDOW  ________________
def parallelogramcode():
  # Creating a custom window
  window = tk.Tk()
  window.geometry("500x380")
  window.config(bg="#858585")
  window.resizable(width=False,height=False)
  window.title('Parallelogram')
  
  # Labels for Heading and Subheadng of GUI
  lb_heading = tk.Label(window,text="Parallelogram Area and Perimeter \n Calculator",font=("Arial", 20),fg="black",bg="#858585")
  lb_subheading = tk.Label(window,font=("Arial",11),text="Please input the side lengths of the Parallelogram you want\nto find the Area and Perimeter of.." ,fg="black",bg="#858585")

  #labels for side length inputs and text boxes
  lb_length = tk.Label(window,font=("Arial",11),text="Length" ,fg="black",bg="#858585")
  lb_width = tk.Label(window,font=("Arial",11),text="Width" ,fg="black",bg="#858585") 
  lb_height = tk.Label(window,font=("Arial",11),text="Height" ,fg="black",bg="#858585")
  lb_area = tk.Label(window,font=("Arial",13),text="Area Calculated:" ,fg="black",bg="#858585")
  lb_perim = tk.Label(window,font=("Arial",13),text="Perimeter Calculated:" ,fg="black",bg="#858585")

  global tbox_area #making tbox_area avaible to use in definitions outisde of trianglecode()
  global tbox_perim #making tbox_perim avaible to use in definitions outisde of trianglecode()
  
  tbox_area=tk.Text(window,width=6,height=1,state="disabled",font=('Arial',24,"bold")) 
  tbox_perim=tk.Text(window,width=6,height=1,state="disabled",font=('Arial',24,"bold"))
    
   # Entry boxes for date, month and year
  global length #making length avaible to use in definitions outisde of trianglecode()
  global width #making width avaible to use in definitions outisde of trianglecode()
  global height #making height avaible to use in definitions outisde of trianglecode()
  
  length = tk.Entry(window,width=15)
  width = tk.Entry(window,width=15)
  height = tk.Entry(window,width=15)
  
  # Button to Open Triangle window
  btn_calculate = tk.Button(window,text="Calculate Area and Perimeter",font=("Arial",11), command=validation)

  # Button to exit application
  btn_exit = tk.Button(window,text="Return to\nShape Chooser",font=("Arial",13),command=window.destroy)
  
  # Placing the elements on the screen with co-ords
  lb_heading.place(x=25,y=5)
  lb_subheading.place(x=24,y=80)
  lb_width.place(x=20,y=165)
  lb_length.place(x=20,y=220)
  lb_height.place(x=20,y=275)
  lb_area.place(x=290,y=130)
  lb_perim.place(x=290,y=220)
  tbox_area.place(x=290,y=165)
  tbox_perim.place(x=290,y=255)
  length.place(x=120,y=165)
  width.place(x=120,y=220)
  height.place(x=120,y=275)
  btn_calculate.place(x=22,y=327)
  btn_exit.place(x=290,y=313)
  