#from  db_sqlite3 import db_connect
from  db_postgres import db_connect

class DB_api:
    def __init__(self,connection_path):
        self.conn=db_connect(connection_path)
        self.cur=self.conn.cursor()

    def execute_and_commit(self,sql,par=()):
        print(sql)
        self.cur.execute(sql,par)
        self.conn.commit()
    
    def execute_and_fetch(self,sql,par=()):
        print(sql)
        self.cur.execute(sql,par)
        rows=self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()
        print("end\n")



