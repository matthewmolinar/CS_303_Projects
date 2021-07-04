# File: ulam_spiral.py
# Description: This program takes a specified size, and displays an ulum spiral based on that size.
# Assignment Number: 11
#
# Name: Matthew Molinar
# EID:  mam24689
# Email: molinar@utexas.edu
# Grader: Skyler
#
# On my honor, Matthew Molinar, this programming assignment is my
# own work and I have not provided this code to any other student.


def main():
    print('This program displays an Ulam Spiral of the specified size.')
    print()
    spiral_size = enter_spiral_size()
    int_spiral = make_int_spiral(spiral_size, spiral_size - 1, spiral_size - 1)
    print('----- The Integer Spiral Size ', spiral_size,' -----', sep = '')
    display_spiral(int_spiral, ' ')
    print()
    ulum_spiral = show_primes(int_spiral)
    print('----- The Ulam Spiral Size ', spiral_size,' -----', sep = '')
    display_spiral(ulum_spiral, '')


def enter_spiral_size():
    n = -2
    while not (n >= 1 and n % 2 == 1):
        n = eval(input('Enter an odd integer greater than or equal to 1: '))
        if not (n >= 1 and n % 2 == 1):
            print(n,' is not an odd integer >= 1.', sep = '')
    return n


def make_int_spiral(spiral_size, row, column):
    spiral = [[0 for c in range(spiral_size)] for r in range(spiral_size)]
    max_number = spiral_size ** 2
    # Row and Column deltas are adapted from Mike Scott's Matrix Checker.
    row_change = [0, -1, 0, 1]
    col_change = [-1, 0, 1, 0]
    # When change_direction(change_counter) is called, and the spiral has run
    # out of room, diagonal_change will provide a diagonal move.
    diagonal_change = ['Up', 'Right', 'Down', 'Left']
    diagonal_counter = 0
    change_counter = 0
    
    # Sending numbers into the initialized matrix to make a spiral.
    while max_number > 0:
        while inbounds(row, column, spiral) and not cell_occupied(row, column, spiral):
            # Change current cell to the current max_number
            spiral[row][column] = max_number
            # Move into that direction
            row = move_row(row, row_change, change_counter)
            column = move_col(column, col_change, change_counter)
            max_number -= 1 
            
        # The spiral needs correction - either it runs out of bounds,
        # or it hits a cell already filled.
        if not inbounds(row, column, spiral) or cell_occupied(row, column, spiral):
            # Make the cell in bounds so we can continue.
            row = make_row_inbounds(row, column, spiral)
            column = make_col_inbounds(row, column, spiral)
            change_counter = change_direction(change_counter)
            # Now move in the new direction.
            row = move_row(row, row_change, change_counter)
            column = move_col(column, col_change, change_counter)
            # If the next cell is occupied, we can 
            # use diagonal_change to make a diagonal move.
            if cell_occupied(row, column, spiral):
                row = move_diag_vertical(row, diagonal_change, diagonal_counter)
                column = move_diag_horizontal(column, diagonal_change, diagonal_counter)
                diagonal_counter = change_direction(diagonal_counter)
    return spiral


# The following code was adapted from Mike's lecture on Conway's
# Game of Life.
# Lets us know if the current cell is within the bounds of the matrix.
def inbounds(row, column, spiral):
    return (0 <= row < len(spiral)) and (0 <= column < len(spiral[row]))
        

# The following code was adapted from Mike's lecture on Conway's
# Game of Life.
def cell_occupied(row, column, spiral):
    if spiral[row][column] == 0:
        return False
    elif spiral[row][column] > 0:
        return True


# If the current row is not in bounds, we make it to be.
def make_row_inbounds(row, column, spiral):
    if row > len(spiral): 
        while row >= len(spiral):
            row -= 1
    elif row < 0:
        while row < 0:
            row += 1
    return row
    

# If the current cell is not inbounds, we make it be.
def make_col_inbounds(row, column, spiral):
    if column >= len(spiral[row]):
        while column >= len(spiral[row]):
            column -= 1
    elif column < 0:
        while column < 0:
            column += 1
    return column


# This function changes the integer used in directions for the spiral.
def change_direction(change_counter):
    change_counter += 1
    if change_counter > 3:
        return change_counter == 0
    else:
        return change_counter


# The following code was adapted from Mike's video on generalizing 
# movement within a list of lists.
def move_row(row, row_change, change_counter):
    r_d = row_change[change_counter]
    row += r_d
    return row


# The following code was adapted from Mike's video on generalizing 
# movement within a list of lists.
def move_col(column, col_change, change_counter):
    r_c = col_change[change_counter]
    column += r_c
    return column


# If the spiral is moving right or left, it needs a vertical correction
# to make a diagonal.
def move_diag_vertical(row, diagonal_change, diagonal_counter):
    d_delta = diagonal_change[diagonal_counter]
    if d_delta == 'Up':
        row -= 1
    elif d_delta == 'Down':
        row += 1
    return row


# To make a diagonal out of a vertical moving line, we add a
# horizontal component.
def move_diag_horizontal(column, diagonal_change, diagonal_counter):
    d_delta = diagonal_change[diagonal_counter]
    if d_delta == 'Right':
        column += 1
    elif d_delta == 'Left':
        column -= 1
    return column


# The following code was adapted from Mike's lecture on Conway's
# Game of Life.
def display_spiral(spiral, separator):
    for r in range(len(spiral)):
        spiral_row = ''
        for c in range(len(spiral[r])):
            # Fence post case.
            if separator == ' ' and c == 0:
                spiral_row += ''
                spiral_row += str(spiral[r][c])
            else:
                spiral_row += separator
                spiral_row += str(spiral[r][c])
        print(spiral_row)


# Converts prime numbers into astericks, none-primes begone!
def show_primes(spiral):
    for r in range(len(spiral)):
        for c in range(len(spiral[r])):
            if is_prime(spiral[r][c]):
                spiral[r][c] = '*'
                pass
            elif not is_prime(spiral[r][c]):
                spiral[r][c] = ' '
    return spiral


# The following code was adopted by the class Textbook. 
# Checks each number fed into it for primeness.
def is_prime(number):
    prime = True
    if number == 1:
        prime = False
        return prime
    for divisor in range(2, int((number / 2) + 1)):
        if number % divisor == 0:
            prime = False
            break
    return prime
    

main()