import psycopg2

def db_connect(connection_path):
    return psycopg2.connect(connection_path)
