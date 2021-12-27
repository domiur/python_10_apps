import sqlite3

def connect():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(name,author,year,isbn):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(name,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * from book ")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="",author="",year="",isbn=""):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * from book where title=? or author=? or year=? or isbn=?",(name,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("DELETE from book where id=?",(id,))
    conn.commit()
    conn.close()


def update(id,name="",author="",year=0,isbn=0):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(name,author,year,isbn,id))
    conn.commit()
    conn.close()


connect()

