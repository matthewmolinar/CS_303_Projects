# File: RPS.py
# Description: This program runs a game of rock paper scissors.
# Assignment Number: 7
#
# Name: Matthew Molinar
# EID:  mam24689
# Email: molinar@utexas.edu
# Grader: Skyler
#
# On my honor, Matthew Molinar, this programming assignment is my own
# work and I have not provided this code to any other student.


import random 


# Asking user for inputs, running rounds, and announcements. 
def main():
    print('Welcome to ROCK PAPER SCISSORS. I, Computer, will be',
        ' your opponent.', sep = '')
    name = get_name()
    round_count = get_round_input()
    use_seed = get_seed_input()

    if use_seed == 'y':
        random.seed(seed_handler())

    print()
    win = 0
    for round in range(1, round_count + 1):
        print('**** Round ', round, ' ****', sep = '')
        print(name, ', enter your choice for this round.', sep = '')
        user_choice = choice_handler()
        computer_choice = random.randint(1,3)
        print('I pick ', computer_bragging(computer_choice), '.', sep = '')
        win = winner_announce(computer_choice, user_choice, win)
    print('We played ', round_count, ' ', grammor_checker(round_count),
        ' of ROCK PAPER SCISSORS.', sep = '')
    print(name, ' won ', win, ' ', grammer_checker(win), '.',
        sep = '')
    print('Well played.')


# This function gets the user's name.
def get_name():
    print('***** INITIAL INPUT *****')
    name = input('Please enter your name: ')
    print('Thank you!')
    print()
    return name


# This function gets the desired round count from the user.
def get_round_input():
    print('***** INITIAL INPUT *****')
    round_count = eval(input('Please enter the number of rounds to play: '))
    print('Thank you!')
    print()
    return round_count

# Asking user if they want to use a seed.
def get_seed_input():
    print('***** INITIAL INPUT *****')
    use_seed = input('Please enter y if you want to set the seed: ')
    print('Thank you!')
    return use_seed
    

# This function gets the seed from the user if they want to use it.
def seed_handler():
    print()
    print('***** INITIAL INPUT *****')
    seed_int = eval(input('Please enter an integer for the seed: '))
    print('Thank you!')
    return seed_int


# This function gets the user's choice.
def choice_handler():
    user_choice = input('R for Rock, P for Paper, S for Scissors: ')

    if user_choice == 'R':
        user_choice = 1
    elif user_choice == 'P':
        user_choice = 2
    elif user_choice == 'S':
        user_choice = 3
    return user_choice


# This function converts the random integers into english.
def computer_bragging(computer_choice):
    if computer_choice == 1:
        return 'Rock'
    elif computer_choice == 2:
        return 'Paper'
    else:
        return 'Scissors'


# This function announces the winner of the round.
def winner_announce(computer_choice, user_choice, win):
    if computer_choice == user_choice:
        print('We picked the same thing. Round is a draw.')
    elif computer_choice == 2 and user_choice == 3:
        print('Scissors cut Paper. You win.')
        win += 1
    elif computer_choice == 2 and user_choice == 1:
        print('Paper covers Rock. I win.')
    elif computer_choice == 1 and user_choice == 3:
        print('Rock breaks Scissors. I win.')
    elif computer_choice == 1 and user_choice == 2:
        print('Paper covers Rock. You win.')
        win += 1
    elif computer_choice == 3 and user_choice == 1:
        print('Rock breaks Scissors. You win.')
        win += 1
    elif computer_choice == 3 and user_choice == 2:
        print('Scissors cut Paper. I win.')
    print()
    return win


# This function checks the grammar of the outro based on rounds.
def grammor_checker(round_count):
    if round_count == 1:
        return 'round'
    else:
        return 'rounds'


# This function checks the grammar of the outro based on wins.
def grammer_checker(win):
    if win == 1:
        return 'round'
    else:
        return 'rounds'
        
        
main()