# File: LaterDate.py
# Description: This program will take a date from the user and ask them
# how far into the future they want to go then it displays that date.
# Assignment Number: 4
#
# Name: Matthew Molinar
# EID:  mam24689
# Email: molinar@utexas.edu
# Grader: Skyler
#
# On my honor, Matthew Molinar, this programming assignment is my own
# work and I have not provided this code to any other student.


# This function takes the current date, and how far the user
# wants to go into the future. Then, it displays the date based on
# how far ahead they went.
def main():
    # Getting user input for date and amount of days to skip.
    print('This program asks for a date and days to skip.')
    print('It then displays the date that many days after the given date.')
    print()
    month = input('Enter the month: ')
    day = eval(input('Enter the day of the month: '))
    year = eval(input('Enter the year: '))
    print()
    skip_amt = eval(input('Enter the number of days to skip: '))

    # Correcting for different scenarios in the string output.
    skip_day = day + skip_amt
    skip_month = month
    skip_year = year
    if skip_amt == 1:
        str_modify = 'day'
    else:
        str_modify = 'days'

    # Changing the month for months that have 31 days in them
    # and changing the year in December.
    if (month == 'January' or month == 'March' or month == 'May' \
        or month == 'July' or month == 'August' or month == 'October' \
        or month == 'December') and skip_day > 31:
        skip_day -= 31
        if month == 'January':
            skip_month = 'February'
        elif month == 'March':
            skip_month = 'April'
        elif month == 'May':
            skip_month = 'June'
        elif month == 'July':
            skip_month = 'August'
        elif month == 'August':
            skip_month = 'September'
        elif month == 'October':
            skip_month = 'November'
        elif month == 'December':
            skip_month = 'January'
            skip_year = year + 1
    # Changing the month for months that have 30 days in them.
    elif (month == 'April' or month == 'June' or month == 'September' \
        or month == 'November') and skip_day > 30:
        skip_day -= 30 
        if month == 'April':
            skip_month = 'May'
        elif month == 'June':
            skip_month = 'July'
        elif month == 'September':
            skip_month = 'October'
        elif month == 'November':
            skip_month = 'December'

    # Changing the month for february based on leap years.
    elif month == 'February':
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if skip_day > 29:
                skip_day -= 29
                skip_month = 'March'
        else:
            if skip_day > 28:
                skip_day -= 28
                skip_month = 'March'
    print()
    print(skip_amt, ' ', str_modify, ' after ', month,
          ' ', day, ', ', year, ' is ', skip_month,
          ' ', skip_day, ', ', skip_year, '.', sep='')
    print()


main()
