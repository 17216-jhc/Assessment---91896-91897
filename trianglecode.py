#_____ IMPORTS ______
from main import * #importing imports from main

#_____ DEFINITIONS _____
def find_perim(s1, s2, s3):
  p=s1+s2+s3 #calculates perimeter using sum of length of side 1, length of side 2 and length of side 3
  perimeter=round(p, 2) #rounds calculated perimeter to 2DP
  return perimeter

def find_area(s1, s2, s3):
  x = float(math.acos((s1*s1+s2*s2-s3*s3)/(2*s1*s2))) #calculates an angle of the triangle inputted using the cos rule
  height = float(sin(x) * s1) #uses angle calculated to calculate area using trigonometry
  a=0.5 * s2 * height #calculates Area using base, height then halving
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
  #Perimeter calculated is inserted into the text box after clearing the previous info in the textbox. 
  tbox_perim.delete('1.0', tk.END)
  tbox_perim.insert(tk.END,perimeter)
  tbox_perim.config(state='disabled')

def validation(): 
  # gets the three entries
  s_1 = side_1.get()
  s_2 = side_2.get()
  s_3 = side_3.get()
  
  msg = '' #makes the message box 'clear'
  
  if len(s_1) == 0 or len (s_2) == 0 or len (s_3) == 0: #checks if the number of characters in the input boxes = 0
    msg = 'Please Do Not leave any Input Boxes Empty' #Inputs the error message that pops up
    calc_area = ' ' #clears the Calc Area box
    display_area(calc_area) #clears calc area box by printing the cleared Calc area box
    calc_perim = ' ' #clears the Calc Perimeter box
    display_perim(calc_perim) #clears calc perim box by printing the cleared the Calc Perimeter box
    
  else:
    try:
      if any(ch.isdigit() for ch in s_1) == False or any(ch.isdigit() for ch in s_2) == False or any(ch.isdigit() for ch in s_3) == False: #checks if the sides inputted by user contain letters or symbols (str)
        msg = 'Side length must be a NUMBER, EG: 5, not "five" or "fifth"' #Inputs the error message that pops up
        calc_area = ' ' #clears the Calc Area box
        display_area(calc_area) #prints cleared the Calc Area box
        calc_perim = ' ' #clears the Calc Perimeter box
        display_perim(calc_perim) #prints cleared the Calc Perimeter box
        
      else:
        #converting inputted sides to float
        s1 = float(s_1)
        s2 = float(s_2)
        s3 = float(s_3)

        if s1 <= 0 or s2 <= 0 or s3 <= 0: #checks that the side lengths inputted are greater than 0
          msg = 'Please Do Not Input a Negative length' #Inputs the error message that pops up
          calc_area = ' ' #clears the Calc Area box
          display_area(calc_area) #prints cleared the Calc Area box
          calc_perim = ' ' #clears the Calc Perimeter box
          display_perim(calc_perim) #prints cleared the Calc Perimeter box
        
        elif (s1 + s2) <= s3 or (s3 + s1) <= s2 or (s3 + s2) <= s1: #checks if the sum of two sides is greater than the third side to check if an inputted triangle is impossible
          msg = 'Sorry, that Triangle is Impossible, Please make the Sum of any Two Sides Equal More than the Third Length' #Inputs the error message that pops up
          calc_area = ' ' #clears the Calc Area box
          display_area(calc_area) #prints cleared the Calc Area box
          calc_perim = ' ' #clears the Calc Perimeter box
          display_perim(calc_perim) #prints cleared the Calc Area box
          
        else:
          calc_area= find_area(s1, s2, s3) #Calculates the area using all three side lengths
          display_area(calc_area) #displays calculated area in in the appropriate tbox
          calc_perim = find_perim(s1, s2, s3) #Calculates the Perimeter using all three side lengths
          display_perim(calc_perim) #displays calculated Perimeter in in the appropriate tbox
    except Exception as ep:
      messagebox.showerror('error', ep) #prints and error message to tell the user and error happened according to the syntax error

  
  if msg != '':
    messagebox.showinfo('message', msg) #tells the program that if the message box is not empty, print the message box with it's new text
    
  # ____________   TRIANGLE WINDOW  ________________
def trianglecode():
  # Creating a custom window
  window = tk.Tk()
  window.geometry("500x380")
  window.config(bg="#858585")
  window.resizable(width=False,height=False)
  window.title('Triangle')
  
  # Labels for Heading and Subheadng of GUI
  lb_heading = tk.Label(window,text="Triangle Area and Perimeter \n Calculator",font=("Arial", 20),fg="black",bg="#858585")
  lb_subheading = tk.Label(window,font=("Arial",11),text="Please input the side lengths of the triangle you want to find\nthe Area and Perimeter of.." ,fg="black",bg="#858585")

  #labels for all of the entry boxes and text boxes
  lb_base = tk.Label(window,font=("Arial",11),text="Side 1 Length" ,fg="black",bg="#858585")
  lb_side_1 = tk.Label(window,font=("Arial",11),text="Side 2 Length" ,fg="black",bg="#858585")
  lb_side_2 = tk.Label(window,font=("Arial",11),text="Side 3 Length" ,fg="black",bg="#858585")
  lb_area = tk.Label(window,font=("Arial",13),text="Area Calculated:" ,fg="black",bg="#858585")
  lb_perim = tk.Label(window,font=("Arial",13),text="Perimeter Calculated:" ,fg="black",bg="#858585")
 
  #text boxes that show the calculated area and perimeter
  global tbox_area
  global tbox_perim
  
  tbox_area=tk.Text(window,width=6,height=1,state="disabled",font=('Arial',24,"bold"))
  tbox_perim=tk.Text(window,width=6,height=1,state="disabled",font=('Arial',24,"bold"))
    
   # Entry boxes for date, month and year
  global side_1
  global side_2
  global side_3
  
  side_1 = tk.Entry(window,width=15)
  
  side_2 = tk.Entry(window,width=15)
  
  side_3 = tk.Entry(window,width=15)
  
  # Button to Open Triangle window
  btn_calculate = tk.Button(window,text="Calculate Area and Perimeter",font=("Arial",11), command=validation)

  # Button to exit application
  btn_exit = tk.Button(window,text="Return to\nShape Chooser",font=("Arial",13),command=window.destroy)
  
  # Placing the elements on the screen with co-ords
  lb_heading.place(x=55,y=5)
  lb_subheading.place(x=22,y=80)
  lb_base.place(x=20,y=165)
  lb_side_1.place(x=20,y=220)
  lb_side_2.place(x=20,y=275)
  lb_area.place(x=290,y=130)
  lb_perim.place(x=290,y=220)
  tbox_area.place(x=290,y=165)
  tbox_perim.place(x=290,y=255)
  side_1.place(x=140,y=165)
  side_2.place(x=140,y=220)
  side_3.place(x=140,y=275)
  btn_calculate.place(x=22,y=327)
  btn_exit.place(x=290,y=313)
  