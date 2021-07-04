# File: Zeller.py
# Description: This program takes a month, day, and year, then returns
# the day of the month.
# Assignment Number: 5
#
# Name: Matthew Molinar
# EID:  mam24689
# Email: molinar@utexas.edu
# Grader: Skyler
#
# On my honor, Matthew Molinar, this programming assignment is my own
# work and I have not provided this code to any other student.


# This function asks for month, day, and year, then returns day of
# the month.
def main():
    # Requesting user to input month, day, and year.
    month = input('Enter the month (for example, January, February, etc.): ')
    day_in_month = eval(input('Enter the day (an integer): '))
    year = eval(input('Enter the year (an integer): '))

    # Setting integers based on months entered.
    if month == 'January':
        month_number = 13
        year -= 1
    elif month == 'February':
        month_number = 14
        year -= 1
    elif month == 'March':
        month_number = 3
    elif month == 'April':
        month_number = 4
    elif month == 'May':
        month_number = 5
    elif month == 'June':
        month_number = 6
    elif month == 'July':
        month_number = 7
    elif month == 'August':
        month_number = 8
    elif month == 'September':
        month_number = 9
    elif month == 'October':
        month_number = 10
    elif month == 'November':
        month_number = 11
    elif month == 'December':
        month_number = 12

    # Calculating values using Zeller's Congruence.
    variation_in_days_per_month = (13 * (month_number + 1)) // 5
    leap_year_days = year // 4 + year // 400
    century_days = year // 100
    total_days = day_in_month + variation_in_days_per_month + year \
                 + leap_year_days - century_days
    day_of_week = total_days % 7

    # Using the values calculated to tell the day of the week.
    if day_of_week == 0:
        day_of_week = 'Saturday'
    elif day_of_week == 1:
        day_of_week = 'Sunday'
    elif day_of_week == 2:
        day_of_week = 'Monday'
    elif day_of_week == 3:
        day_of_week = 'Tuesday'
    elif day_of_week == 4:
        day_of_week = 'Wednesday'
    elif day_of_week == 5:
        day_of_week = 'Thursday'
    elif day_of_week == 6:
        day_of_week = 'Friday'
    print('The day of the week is ', day_of_week, '.', sep='')


main()