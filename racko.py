# File: racko.py
# Description: A program that simulates the card and number game
# Rack-O. Players use the keyboard and take turns.
# Assignment Number: 10
#
# Name: Matthew Molinar
# EID:  mam24689
# Email: molinar@utexas.edu
# Grader: Skyler
#
# On my honor, Matthew Molinar, this programming assignment is my
# own work and I have not provided this code to any other student. 


import random


# Play one game of Rack-O.
def main():
    # Get the rack size, create the deck, and deal the initial racks.
    rack_size = prep_game()
    deck = list(range(1, 61))
    random.shuffle(deck)
    player = 1
    player_1_rack = get_rack(deck, rack_size)
    player_2_rack = get_rack(deck, rack_size)
    discard = [deck.pop(0)]

    # Begin the round. Keep track of who's turn it is.
    while not is_sorted(player_1_rack) and not is_sorted(player_2_rack):
        print()
        # Checking to see if deck is empty.
        if not deck:
            print('Deck is empty. Shuffling discard pile.')
            random.shuffle(discard)
            deck = discard
            discard = [deck.pop(0)]
        print('Player ', player, '\'s turn.', sep = '')
        if player == 1:
            take_turn(deck, discard, player_1_rack)
            player = 2
        else:
            take_turn(deck, discard, player_2_rack)
            player = 1
    print()
    print('Player', 1 if player == 2 else 2, 'wins!')
    

# Get ready to play 1 game.
# Show the instructions if the user wants to see them.
# Set the seed for the random number generator.
# Return the size of the rack to use.
def prep_game():
    print('----- Welcome to Rack - O! -----')
    if input('Enter y to display instructions: ') == 'y':
        instructions()
    print()
    random.seed(eval(input('Enter number for initial seed: ')))
    rack_size = eval(input('Enter the size of the rack to use. '
                            + 'Must be between 5 and 10: '))
    while not 5 <= rack_size <= 10:
        print(rack_size, 'is not a valid rack size.')
        rack_size = eval(input('Enter the size of the rack to use. '
                            + 'Must be between 5 and 10: '))
    return rack_size


# Print the instructions of the game.
def instructions():
    print()
    print('The goal of the game is to get the cards in your rack of cards')
    print('into ascending order. Your rack has ten slots numbered 1 to 10.')
    print('During your turn you can draw the top card of the deck or take')
    print('the top card of the discard pile.')
    print('If you draw the top card of the deck, you can use that card to')
    print('replace a card in one slot of your rack. The replaced card goes to')
    print('the discard pile.')
    print('Alternatively you can simply choose to discard the drawn card.')
    print('If you take the top card of the discard pile you must use it to')
    print('replace a card in one slot of your rack. The replaced card goes')
    print('to the top of the discard pile.')


# Take the player's turn. Give them the choice of drawing or taking
# the top card of the discard pile. If they draw they can replace
# a card or discard the draw. If they take the top card of the discard
# pile they must replace a card in their rack.
# player loses turn if they discard the drawn card
# if player outright takes the discard pile, they must replace a card.
def take_turn(deck, discard, player_rack):
    print('Your current rack ', player_rack)
    print('Top of discard pile ', discard[0])
    # Player can choose to draw or to take from discard pile.
    if input('Enter d to draw anything else to take top' \
        + ' of discard pile: ') == 'd':
        new_card = deck.pop(0)
        print()
        print('drew the', new_card)
        # Player can choose to replace a card with the card they drew
        # or to discard it.
        if input('Enter p to place card, anything else' \
            + ' to discard it: ') == 'p':
            place_card(player_rack, new_card, discard)
        else:
            discard.insert(0, new_card)
            print('The rack after the turn ', player_rack)
    else:
        new_card = discard.pop(0)
        print()
        place_card(player_rack, new_card, discard)
        

# Ask the player which card to replace in their rack.
# Replace it with the given new card. Place the card removed
# from the player's rack at the top of the discard pile.
# Error checks until player enters a card that is currently
# in their rack.
def place_card(player_rack, new_card, discard):
    replacement_found = False
    while not replacement_found:
        replace_card = eval(input('Enter the card number to replace' \
            + ' with the ' + str(new_card) + ': '))
        for card in range(0, len(player_rack)):
            # Searches the player's rack for the card they want.
            # If it is found, search ends. If it isn't, they
            # have to select a new card.
            if player_rack[card] == replace_card:
                replacement_found = True
                player_rack.insert(card, new_card)
                discard.insert(0, player_rack.pop(card + 1))
                print('The rack after the turn ', player_rack)
                break
        if not replacement_found: print(replace_card, 'is not in your rack.')
            
           
# Return True if this rack is sorted in ascending order, False otherwise.
# Do not create any new lists in this function.
def is_sorted(rack):
    i = 1
    while i < len(rack):
        if rack[i] < rack[i - 1]:
            return False
        else:
            i += 1
    return True
    

# Deal the top 10 cards of the deck into a new rack. The first
# card goes in the first slot, the second card goes in the second
# slot, and so forth. We assume len(deck) >= rack_size. Return the
# list of ints representing the rack.
def get_rack(deck, rack_size):
    player_deck = []
    i = 0
    while i < rack_size: 
        player_deck.append(deck.pop(0))
        i += 1
    return player_deck


main()