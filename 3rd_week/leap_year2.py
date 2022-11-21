# year = 1752
# print("Enter a year after 1752:")
# response = int(input(""))
# if response % 4:
#     print(f"{response} is a leap year!")
# elif response % 400:
#     print(f"{response} is a leap year!")
# elif response % 100:
#     print(f"{response} is not a leap year!")

# def leap_year(year):
#     leap = False
#     if year % 400 == 0 and year % 100 == 0:
#         print('{0}is a leap year!'.format(year))
#     elif year % 4 == 0 and year % 100 != 0:
#         print('{0}is a leap year!'.format(year))

def leap_year(year):
    if year % 400 == 0 and year % 100 == 0:
       return f'{True} it is a leap year!'
    elif year % 4 == 0 and year % 100 != 0:
        return f'{True} it is a leap year!'
    else:
        return f'{False} it is not a leap year!'
year = int(input(f'Enter year to see if its a leap year: '))
print(leap_year(year))

def print_month_calendar(month, year, days_in_month, start_of_day):
    month_string = f'{month} {year}'

    print(f'\n{month_string:^32}\n')
    print('   S   M   T   W   T   F   S')
    
    print('    ' * start_of_day, end='')
    
    for day in range(1, days_in_month + 1):
        print(f'{day:>4}', end='')
        if (day + start_of_day) % 7 == 0:
            print('\n')
print_month_calendar('September', 2021, 30, 3)