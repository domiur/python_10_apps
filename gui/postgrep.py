import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='testpydb' user='testpyuser' password='test123test' host='localhost' port=5432 ")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(name TEXT,num INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insert(item,num,price):
    conn=psycopg2.connect("dbname='testpydb' user='testpyuser' password='test123test' host='localhost' port=5432 ")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item,num,price))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='testpydb' user='testpyuser' password='test123test' host='localhost' port=5432 ")
    cur=conn.cursor()
    cur.execute("select * FROM store")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='testpydb' user='testpyuser' password='test123test' host='localhost' port=5432 ")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE name=%s",(item,))
    conn.commit()
    conn.close()

def update(item,num,price):
    conn=psycopg2.connect("dbname='testpydb' user='testpyuser' password='test123test' host='localhost' port=5432 ")
    cur=conn.cursor()
    cur.execute("UPDATE store SET num=%s,price=%s WHERE name=%s",(num,price,item))
    conn.commit()
    conn.close()

create_table()
#insert("book2",8,1.4)
#insert('book asdjl', 20, 105.6)

print (view())
delete("book2")
update('book asdjl', 20, 105.6)
print (view())