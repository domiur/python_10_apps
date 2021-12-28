import sqlite3

def db_connect(connection_path):
    return sqlite3.connect(connection_path)


