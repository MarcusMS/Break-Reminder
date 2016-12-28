import sys
from tkinter import *
from tkinter import messagebox, colorchooser
from tkinter import ttk
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
global endv
endv = 0

root.geometry('400x200+200+100')
root.resizable(False, False)
root.title('Break Reminder')

#defining functions

def mColor():
    global mycolor
    mycolor = colorchooser.askcolor()
    mycolor = mycolor[1]
    return mycolor


    
def second_window():
    global endv
    endv = 0
    top = Toplevel()
    top.geometry('200x100+200+100')
    top.resizable(False, False)

    def shut_up():
        global endv
        endv +=1
        print (endv)
        
        top.destroy()
    

    def video_break():
        global endv
        global time_str
        try:
            break_time= int(spinbox1.get())#*60
        except:
            messagebox.showerror(title="Wrong value", message="Type in the desired amount of minutes as whole numbers")
            return
        
        break_number = int(spinbox2.get())
        while break_number > 0:
            for t in range(break_time, -1, -1):
                sf = "{:02d}:{:02d}".format(*divmod(t, 60))
                time_str.set(sf)
                
                if endv > 0:
                    
                    time_str.set("00:00")
                    break
                top.update()
                ts(1)               
            if endv > 0:
                break   
            
            wo("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
            break_number -= 1
                
        
    label_font = ('helvetica', 40)
    
    clock = Label(top, textvariable=time_str, font=label_font, bg='white', 
         fg=mycolor, relief='raised', bd=3).pack(fill='x', padx=5, pady=5)
    AbortButton = Button(top, text='Abort', command = shut_up).place(x=125, y=75)
    StartButton = Button(top, text='Start', command = video_break).place(x=25, y=75)
    break_number = int(spinbox2.get())
    
   



def exitus():
    mExit = messagebox.askyesno(title="Ending program", message="This will end the program!\nAre You serious?")
    if mExit > 0:
        root.destroy()
        return

        
time_str = StringVar()

blank = Label(root, bg='white', relief='raised', bd=3)
blank.place(x=5, y=5, height = 68, width = 390)

mButton = Button(root, text='Set up breaks', command = second_window)
mButton.place(x=0, y=125)
spinbox1=ttk.Combobox(root, textvariable=break_time, width=17, values=[10, 30, 60, 90, 120])
spinbox1.place(x=0, y=100)
spinbox2=Spinbox(root, from_=1, to=60, state=NORMAL, wrap=True, textvariable=break_number)
spinbox2.place(x=200, y=100)
label_minutes = Label(root, text='Take a break every:')
label_minutes2 = Label(root, text=' minutes')
label_minutes.place(x=0, y=80)
label_minutes2.place(x=130, y=100)
label_times = Label(root, text='time(s)')
label_times.place(x=340, y=100)

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
