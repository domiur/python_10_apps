from db_api import DB_api
from db_factory import db_connect

class Database:
    schema=["id:INTEGER PRIMARY KEY",
            "title:TEXT",
            "author:TEXT",
            "year:INTEGER",
            "isbn:INTEGER"]

    def __init__(self,dbtype,dbpath,dbname):
        self.connection_path=dbpath
        self.dbname=dbname
        self.connect(dbtype)
        self.create_table()

    def connect(self,dbtype):
        self.db=DB_api(db_connect(dbtype),self.connection_path)

    def create_table(self):
        self.db.execute_and_commit("CREATE TABLE IF NOT EXISTS "+self.dbname+
            " ("+
            ','.join([ i.replace(':',' ') for i in Database.schema])+
            ")")

    def insert(self,name,author,year,isbn):
        self.db.execute_and_commit("INSERT INTO "+self.dbname+" VALUES(NULL,'%s','%s','%s','%s')" % (name,author,year,isbn))

    def view(self):
        return self.db.execute_and_fetch("SELECT * from "+self.dbname)

    def search(self,name="",author="",year="",isbn=""):
        return self.db.execute_and_fetch("SELECT * from "+self.dbname+
                " where title='%s' or author='%s' or year='%s' or isbn='%s'" % (name,author,year,isbn))

    def getid(self,name="",author="",year="",isbn=""):
        rows=self.db.execute_and_fetch("SELECT * from "+self.dbname+
                " where title='%s' and author='%s' and year='%s' and isbn='%s'" % (name,author,year,isbn))
        if rows is not None and len(rows)>0:
            return rows[0][0]
        else:
            return None

    def delete(self,id):
        self.db.execute_and_commit("DELETE from "+self.dbname+" where id='%s'" % (id))

    def update(self,id,name="",author="",year=0,isbn=0):
        self.db.execute_and_commit("UPDATE "+self.dbname+
                " SET title='%s', author='%s', year='%s', isbn='%s' WHERE id='%s'" % (name,author,year,isbn,id))




