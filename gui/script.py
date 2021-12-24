from tkinter import *

window=Tk()

def press_button():
    print(e1_value.get())
    t1.insert(END,e1_value.get())
    
b1=Button(window,text="run",command=press_button)
b1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=2,width=20)
t1.grid(row=0,column=2)

window.mainloop()