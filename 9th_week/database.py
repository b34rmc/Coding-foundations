import sqlite3
from create_class import User

create_user_table = '''
CREATE TABLE IF NOT EXISTS User (
    user_id UNIQUE PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    city TEXT,
    state TEXT,
    email TEXT NOT NULL UNIQUE,
    password TEXT,
    date_created TEXT)
'''
    
insert_user = '''INSERT INTO User (user_id,first_name,last_name,city,state,email,password,date_created)
    VALUES (?,?,?,?,?,?,?,?);'''
    
select_user_by_id = "SELECT * FROM User WHERE user_id = ?;"



def connect():
    return sqlite3.connect("capstone.db")


def create_tables(connection):
    with connection:
        connection.execute(create_user_table)
    
def add_user(connection, user_id, first_name, last_name, city, state, email, password, date_created):
    with connection:
        connection.execute(insert_user, (user_id, first_name, last_name, city, state, email, password, date_created))
        
def get_user(connection, id):
    with connection:
        return connection.execute(select_user_by_id, (id,)).fetchone()