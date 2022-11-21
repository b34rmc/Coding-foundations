# month = "September"
# year = " 2021"
# month_year = month, year
# days = "S   M   T   W   T   F   S"
# weekone = "1   2   3   4"
# weektwo = "5   6   7   8   9  10  11"
# weekthree = "12  13  14  15  16  17  18"
# weekfour =  "19  20  21  22  23  24  25"
# weekfive =  "26  27  28  29  30"

# print(f"\n{month_year:^35}\n")
# print(f"{days:^35}\n")
# print(f"{weekone:>30}\n")
# print(f"{weektwo:>30}\n")
# print(f"{weekthree:>30}\n ")
# print(f"{weekfour:>30}\n")
# print(f"{weekfive:>22}\n")


# def month_calendar(month, year, day, daysInMonth):
#     month = "September"
#     year = " 2021"
# month_year = month, year
# day = 'Wednesday'
# days = "S   M   T   W   T   F   S"
# weekone = "1   2   3   4"
# weektwo = "5   6   7   8   9  10  11"
# weekthree = "12  13  14  15  16  17  18"
# weekfour =  "19  20  21  22  23  24  25"
# weekfive =  "26  27  28  29  30"

# def print_month_calendar(month, year, days_in_month, start_of_day):
#     month_string = f'{month} {year}'

#     print(f'\n{month_string:^32}\n')
#     print('   S   M   T   W   T   F   S')
    
#     print('    ' * start_of_day, end='')
    
#     for day in range(1, days_in_month + 1):
#         print(f'{day:>4}', end='')
#         if (day + start_of_day) % 7 == 0:
#             print('\n')
# print_month_calendar('September', 2021, 30, 3)
        