import sqlite3
from faker import Faker
fake = Faker()

connection = sqlite3.connect('Phone_book.db')
cursor = connection.cursor()

def create_schema(cursor):
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS People (
                       person_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       first_name TEXT NOT NULL,
                       last_name TEXT,
                       city TEXT,
                       state TEXT,
                       phone_number INTEGER NOT NULL
                   )
                   '''),
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Birthdays (
                       person_id INTEGER,
                       birthdate INTEGER,
                       birth_place TEXT,
                       FOREIGN KEY (
                           person_id
                       )
                       REFERENCES People (person_id),
                       PRIMARY KEY (
                           person_id
                       )
                   )
                   ''')

create_schema(cursor)
connection.commit()

count = 25

def insertPeople():
    people = []
    for i in range(count):
        people.append([fake.first_name(),fake.last_name(),fake.city(),fake.state(),fake.phone_number()])

    cursor.executemany('''
    INSERT INTO People (First_name, Last_name, City, State, Phone_number)
    VALUES (?,?,?,?,?)''', people)


def addBirthday():
    bday = []
    for i in range(count):
        bday.append([fake.date(), fake.city()])
        
    cursor.executemany('''
                       INSERT INTO Birthdays (birthdate, birth_place)
                       VALUES(?,?)''',bday)

   
    
    # name_input = input('Enter your name')
    # birthday_input = input('Enter your name')
    # birthday_year_input = input('Enter your name')
    # connection = sqlite3.connect('friends_phonebook.db)
    # values = (name_input, birthday_input, birthday_year_input)
    #  connection.commit()
    