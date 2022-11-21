import sqlite3
connection = sqlite3.connect('registrations.db')
cursor = connection.cursor()

def create_schema(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS People (
        person_id   INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name  TEXT    NOT NULL,
        last_name   TEXT,
        email               UNIQUE
                            NOT NULL,
        phone       TEXT,
        password    TEXT    NOT NULL,
        address     TEXT,
        city        TEXT,
        state       TEXT,
        postal_code TEXT,
        active      INTEGER DEFAULT 1
        );
    ''')
    
    cursor.execute ('''
                    CREATE TABLE IF NOT EXISTS Cohorts (
        cohort_id     INTEGER PRIMARY KEY AUTOINCREMENT,
        instructor_id INTEGER REFERENCES People (person_id),
        course_id     INTEGER REFERENCES Courses (course_id),
        start_date    TEXT,
        end_date      TEXT,
        active        INTEGER DEFAULT (1) 
        );
                    ''')
    
    cursor.execute ('''
                    CREATE TABLE IF NOT EXISTS Courses (
    course_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL,
    description TEXT    NOT NULL,
    active      INTEGER DEFAULT 1
);

                    ''')
    
    cursor.execute ('''
                    CREATE TABLE IF NOT EXISTS Student_Cohort_Registrations (
        student_id        INTEGER NOT NULL,
        cohort_id         INTEGER NOT NULL,
        registration_date TEXT    NOT NULL,
        completion_date   TEXT,
        drop_date         TEXT,
        active            INTEGER DEFAULT (1),
        FOREIGN KEY (
            student_id
        )
        REFERENCES People (person_id),
        FOREIGN KEY (
            cohort_id
        )
        REFERENCES Cohorts (cohort_id),
        PRIMARY KEY (
            student_id,
            cohort_id
        )
        );
                    ''')
    

        
        
        

result = create_schema(cursor)
