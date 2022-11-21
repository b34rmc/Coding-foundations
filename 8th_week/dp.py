# import sqlite3

# connection = sqlite3.connect('registrations.db')
# cursor = connection.cursor()

import re


def isValid(field, regex):
    if not re.fullmatch(regex, field):
      return ''
    return field

def add_person():    
    first_name = ''
    while not first_name:
        first_name = input('Enter first name:')
        
    last_name = input('Enter last name:')
    email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    email = ''
    while not email:
        email = input('Enter Email:')
        email = isValid(email, email_regex)
        
    phone = input('Enter phone #:')
    password = ""
    while not password:
        password = input('Enter password:')
    address = input('Enter address:')
    city = input('Enter city:')
    state = input('Enter state:')
    postal_code = input('Enter postal code:')
    

def add_course():
    print('add course')
    pass

def add_cohort():
    '''
    The user must select
    an existing person as the instructor
    an existing course as the course
    '''
    pass

def assign_cohort():
    '''
    select an existing person as the student
    and existing cohort as the cohort
    '''
    pass
    
def rem_cohort():
    '''
    this should just set the student_cohort
    registration record as active = 0 and set
    the drop date to today
    '''
    pass

def deactivate_course():
    '''
    it can no longer be selected
    for a new cohort
    '''
    pass

def deactivate_person():
    '''
    they can no longer be selected 
    for new registrations or as an 
    instructor for a cohort
    '''
    pass
    
def deactivate_cohort():
    '''
    they can no longer be selected 
    for new student registrations
    '''
    pass

def completed_course():
    '''
    this will set the completion date
    on the student_cohort_registration
    '''
    pass

def reactivate():
    pass

def view_active_reg():
    pass

def view_active_cohorts():
    pass

def view_active_ppl():
    pass


def menu():
    print('''
          Welcome to Student Registration\n\n
          (1) Create Person
          (2) Create Course
          ''')
    ui = input("What would you like to do? (1-14):\n")
    
    if ui == '1':
        add_person()
    elif ui == '2':
        add_course()

menu()