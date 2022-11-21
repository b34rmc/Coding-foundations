import sqlite3
from sqlite3 import Error

connection = sqlite3.connect('Altering_Tables.db')
cursor = connection.cursor()


def create_schema(cursor):
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Persons (
                       person_id INTEGER PRIMARY KEY,
                       first_name TEXT,
                       last_name TEXT,
                       stage_name TEXT,
                       birthdate TEXT
                   )
                   ''');
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Movies (
                       movie_id INTEGER PRIMARY KEY,
                       name TEXT UNIQUE,
                       production_company TEXT,
                       director INTEGER,
                       release_date TEXT,
                       FOREIGN KEY (director)
                       REFERENCES Persons (person_id),
                       PRIMARY KEY(person_id)
                       
                )
                   ''');
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Actors (
                       person_id INTEGER,
                       movie_id INTEGER,
                       character_name TEXT,
                       is_lead_role INTEGER,
                       FOREIGN KEY (person_id)
                       REFERENCES Persons (person_id),
                       FOREIGN KEY (movie_id)
                       REFERENCES Movies (movie_id),
                       PRIMARY KEY (
                           person_id,
                           movie_id
                       )
                   )
                   ''')
    
    query = '''INSERT INTO Persons (first_name, last_name, stage_name, birthdate)
            VALUES(?,?,?,?)'''
    values = [
        ('Robert', 'Downey Jr.', 'Iron Man', 'April 4, 1965'),
        ('SCARLETT', 'Johansson', 'Natasha Romanoff', 'November 22, 1984'),
        ('Chris', 'Hemsworth', 'Thor', 'August 11, 1983'),
        ('Joe', 'Russo', '', ''),
        ('Joss', 'Whedon', '', ''),
        ('Anthony', 'Russo', '', '')
    ]
    
    cursor.executemany(query,values)
    connection.commit()
    connection.close()
    # cursor.execute('''
    #         INSERT INTO Persons (first_name, last_name, stage_name, birthdate)
    #         VALUES 
    #                 ('Robert', 'Downey Jr.', 'Iron Man', 'April 4, 1965'),
    #                 ('SCARLETT', 'Johansson', 'Natasha Romanoff', 'November 22, 1984'),
    #                 ('Chris', 'Hemsworth', 'Thor', 'August 11, 1983'),
    #                 ('Joe', 'Russo', '', ''),
    #                 ('Joss', 'Whedon', '', ''),
    #                 ('Anthony', 'Russo', '', '');
    #         ''');
    

create_schema(cursor)

