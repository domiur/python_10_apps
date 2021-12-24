from tkinter import *

win=Tk()

def but_run():
    val=float(e1_var.get())
    t1.delete(1.0,END)
    t1.insert(END,val*1000)
    t2.delete(1.0,END)
    t2.insert(END,val*2.2)
    t3.delete(1.0,END)
    t3.insert(END,val*35)


l1=Label(win,text="kg")
l1.grid(row=0,column=1)
e1_var=StringVar()
e1=Entry(win,textvariable=e1_var)
e1.grid(row=0,column=2)
b1=Button(win,text="run",command=but_run)
b1.grid(row=0,column=3)



t1=Text(win,height=1,width=20)
t1.grid(row=1,column=1)
t2=Text(win,height=1,width=20)
t2.grid(row=1,column=2)
t3=Text(win,height=1,width=20)
t3.grid(row=1,column=3)

win.mainloop()