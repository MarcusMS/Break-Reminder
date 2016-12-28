import sys
from tkinter import *
from tkinter import messagebox, colorchooser
from time import sleep as ts
from webbrowser import open as wo

root = Tk()

#defining variables
global break_number
break_number = IntVar(root)
break_number.set(3)
global break_time
break_time = IntVar(root)
break_time.set(10)
mycolor="black"


root.geometry('400x200+200+100')
root.resizable(False, False)
root.title('Break Reminder')

#defining functions

def mColor():
    global mycolor
    mycolor = colorchooser.askcolor()
    mycolor = mycolor[1]
    return mycolor
    

def timer():

    break_time= int(spinbox1.get())
    break_number = int(spinbox2.get())
    for t in range(break_time, -1, -1):
        
        sf = "{:02d}:{:02d}".format(*divmod(t, 60))
        time_str.set(sf)
        root.update()
        ts(1)
        

def video_break():
    clock()
    break_time= int(spinbox1.get())
    break_number = int(spinbox2.get())
    
    while break_number > 0:
        timer()
        ts(break_time)
        wo("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
        break_number -= 1

def exitus():
    mExit = messagebox.askyesno(title="Ending program", message="This will end the program!\nAre You serious?")
    if mExit > 0:
        root.destroy()
        return

def clock():
    label_font = ('helvetica', 40)
    clock = Label(root, textvariable=time_str, font=label_font, bg='white', 
         fg=mycolor, relief='raised', bd=3)
    clock.place(x=5, y=5, height = 68, width = 390)
    return
        
time_str = StringVar()

blank = Label(root, textvariable=time_str, bg='white', relief='raised', bd=3)
blank.place(x=5, y=5, height = 68, width = 390)

mButton = Button(root, text='Set up breaks', command = video_break)
mButton.place(x=0, y=125)
spinbox1=Spinbox(root, from_=1, to=60, state=NORMAL, wrap=True, textvariable=break_time)
spinbox1.place(x=0, y=100)
spinbox2=Spinbox(root, from_=1, to=60, state=NORMAL, wrap=True, textvariable=break_number)
spinbox2.place(x=200, y=100)
label_minutes = Label(root, text='Take a break every:')
label_minutes2 = Label(root, text=' minutes')
label_minutes.place(x=0, y=80)
label_minutes2.place(x=135, y=100)

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Change Clock Colour", command=mColor)
filemenu.add_command(label="Close", command=exitus)

menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help")
helpmenu.add_command(label="About")

menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.mainloop()
