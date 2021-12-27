from tkinter import *
import bookstore_backend

window=Tk()

l1=Label(window,text="Title")
l2=Label(window,text="Author")
l3=Label(window,text="Year")
l4=Label(window,text="ISBN")

l1.grid(row=0,column=0)
l2.grid(row=0,column=2)
l3.grid(row=1,column=0)
l4.grid(row=1,column=2)

title_var=StringVar()
e1=Entry(window,textvariable=title_var)
author_var=StringVar()
e2=Entry(window,textvariable=author_var)
year_var=StringVar()
e3=Entry(window,textvariable=year_var)
isbn_var=StringVar()
e4=Entry(window,textvariable=isbn_var)

e1.grid(row=0,column=1)
e2.grid(row=0,column=3)
e3.grid(row=1,column=1)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window,width=30)
sb1.grid(row=2,column=2,rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

def command_view():
    list1.delete(0,END)
    for row in bookstore_backend.view():
        list1.insert(END,row)

def command_search():
    list1.delete(0,END)
    name,author,year,isbn=title_var.get(),author_var.get(),year_var.get(),isbn_var.get()
    for row in bookstore_backend.search(name,author,year,isbn):
        list1.insert(END,row)

def command_add():
    name,author,year,isbn=title_var.get(),author_var.get(),year_var.get(),isbn_var.get()
    bookstore_backend.insert(name,author,year,isbn)
    command_view()

def command_delete():
    name,author,year,isbn=title_var.get(),author_var.get(),year_var.get(),isbn_var.get()
    bookstore_backend.insert(name,author,year,isbn)
    command_view()

b1=Button(window,text="View all",width=12,command=command_view)
b2=Button(window,text="Search entry",width=12,command=command_search)
b3=Button(window,text="Add entry",width=12,command=command_add)
b4=Button(window,text="Update selected",width=12)
b5=Button(window,text="Delete selected",width=12,command=command_delete)
b6=Button(window,text="Close",width=12)

b1.grid(row=2,column=3)
b2.grid(row=3,column=3)
b3.grid(row=4,column=3)
b4.grid(row=5,column=3)
b5.grid(row=6,column=3)
b6.grid(row=7,column=3)

window.mainloop()