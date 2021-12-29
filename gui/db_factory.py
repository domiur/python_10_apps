import  db_sqlite3 
import  db_postgres 

def db_connect(dbtype="sqlite3"):
    if dbtype=="sqlite3":
        return db_sqlite3.db_connect
    elif dbtype=="postgres":
        return db_postgres.db_connect
    print('unknown DB type')
    return None

    