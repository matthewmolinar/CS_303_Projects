# File: Dice.py
# Description: This program simulates the game of craps using dice.
# Assignment Number: 6
#
# Name: Matthew Molinar
# EID:  mam24689
# Email: molinar@utexas.edu
# Grader: Skyler
#
# On my honor, Matthew Molinar, this programming assignment is my own
# work and I have not provided this code to any other student.


import random


# This program asks for input such as seed, number of rounds, and
# gives statistics about the game of craps.
def main():
    print('This program simulates the dice game of craps.')
    is_seed = input('Do you want to set the seed? Enter y for yes, ' \
        + 'anything else for no: ')
    
    # Setting the seed for the randomly generated values.
    if is_seed == 'y':
        not_so_random = eval(input('Enter an int for the initial seed: '))
        random.seed(not_so_random)
    
    # Simulating the rounds of craps.
    round_count = eval(input('Enter the number of rounds to run: '))
    if round_count > 0:
        score = 0
        round_counter = 0
        max_roll = 0
        while round_counter < round_count:
            roll_num = 1
            dice_1 = random.randint(1,6)
            dice_2 = random.randint(1,6)
            initial_roll = dice_1 + dice_2

            # Player wins a round.
            if initial_roll == 7 or initial_roll == 11:
                score += 1
                round_counter += 1
            # Player loses a round.
            elif initial_roll == 2 or initial_roll == 3 or initial_roll == 12:
                round_counter += 1
            # Player rolls into point.
            else:
                point = True
                while point:
                    roll_num += 1
                    dice_1 = random.randint(1,6)
                    dice_2 = random.randint(1,6)
                    point_roll = dice_1 + dice_2

                    # Player loses the round.
                    if point_roll == 7:
                        point = False
                    # Player wins the round.
                    elif point_roll == initial_roll:
                        point = False
                        score += 1

                # Updating the maximum rolls.
                if roll_num > max_roll:
                    max_roll = roll_num
                round_counter += 1
    else:
        score = 0
        round_count = 0
        max_roll = 0   
    print('Player won ', score, ' times in ', round_count, ' rounds.', sep='')
    print('Maximum number of rolls in a round = ', max_roll, sep='')


main()


# Analysis 1:
# Yes, the simulation does support that the casinos win in the
# long-term. After the house deals 10,000 games, if each bet was $10
# then the players would win somewhere around 4800-4900 rounds. The 
# casino statistically wins a little more than 50% of the games.
# To win long-term, the house needs to win more than half the time
# because a 50% win-rate breaks even.

# Analysis 2:
# No, I would not play craps with my money. By the end of the
# 500 rounds I would have less than I started with. Optimistically,
# I would gain a small amount of money. On 500
# rounds my simulation won between 220-250. So the casino
# usually walked away with a 50< % win-rate. On 235 rounds won,
# I would be at 4,700$, but then the casino takes away 2,650$.
# After gambling, I am left with 2,050$ which is a very small
# positive return, and not even guaranteed since there's a
# good chance the casino takes more since many times my
# simulation won around 220 rounds.




