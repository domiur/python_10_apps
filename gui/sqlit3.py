import sqlite3


def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(name TEXT,num INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insert(item,num,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,num,price))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("select * FROM store")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE name=?",(item,))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def update(item,num,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET num=?,price=? WHERE name=?",(num,price,item))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

#insert("book2",8,1.4)
print (view())
#delete("book2")
update('book asdjl', 20, 105.6)
print (view())