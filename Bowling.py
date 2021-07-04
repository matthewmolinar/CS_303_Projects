# File: Bowling.py
# Description: This program calculates the average
# and handicap for bowlers.
# Assignment Number: 3
#
# Name: Matthew Molinar
# EID:  mam24689
# Email: molinar@utexas.edu
# Grader: Skyler
# Slip days used this assignment: 0
#
# On my honor, Matthew Molinar, this programming assignment is my own
# work and I have not provided this code to any other student.

import math


# This function calculates the average and handicap for a bowler.
def main():
    # Asking for user input.
    name = input('Enter your name: ')
    print()
    game_1 = eval(input('Enter Game 1: '))
    game_2 = eval(input('Enter Game 2: '))
    game_3 = eval(input('Enter Game 3: '))
    
    # Computing the average of the bowler.
    bowler_sum = game_1 + game_2 + game_3
    bowler_avg = math.floor(bowler_sum / 3)
    
    # Computing the handicap of the bowler.
    bowler_handicap = math.floor((200 - bowler_avg) * .80)
    print()
    
    # Displaying data for the user.
    print(name + '\'s average is: ' + str(bowler_avg))
    print(name + '\'s handicap is: ' + str(bowler_handicap))
    print()
    
    
main()
