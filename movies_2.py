# File: movies_2.py
# Description: A program uses dictionaries to find what words
# appear in reviews with good and bad ratings,
# as well as the length of good and bad reviews.
# Based on the Nifty Assignment:
# http://nifty.stanford.edu/2016/manley-urness-movie-review-sentiment/
# Assignment Number: 13
#
# Name: Matthew
# EID:  Molinar
# Email: molinar@utexas.edu
# Grader: Skyler
#
# On my honor, Matthew Molinar, this programming assignment is my
# own work and I have not provided this code to any other student.


# Read the main data file and run the menu loop.
def main():
    print('Welcome to the movie sentiment program - Version 2.')
    file_name = input('Enter file name with reviews: ')
    words_dictionary, num_words_dictionary = get_dictionaries(file_name)
    choice = get_choice()
    while '1' <= choice <= '3':
        # Get the index of the function to call.
        if choice == '1':
            show_individual_stats(words_dictionary, 'a word')
        elif choice == '2':
            cutoff_stats(words_dictionary)
        else:
            show_individual_stats(num_words_dictionary, 'the number of words')
        choice = get_choice()

    
# Display the menu and get the users choice.
# Returns the user's choice as a String.
def get_choice():
    print()
    print('OPTIONS:')
    print('1. See statistics for a given word.')
    print('2. See all words that meet given cut-offs.')
    print('3. See statistics for reviews with a given number of words.')
    print('4. Or anything else to quit.')
    result = input('Please enter your choice: ')
    print()
    return result


# Given the file name, create and return two dictionaries.
# All strings in reviews are shifted to lower case.
#
# The first dictionary has keys that are words (any and all
# strings in the reviews) with the value a list of length 2.
# Both elements of the list are integers.
# The first element in the list is the number of reviews that
# contain the word (key) and the second is the sum of all the
# review scores that contain the word (key). 
# 
# The second dictionary has keys that are also strings representing
# the number of words (any and all strings) in a review.
# So for example '12' if the review has 12 words. The value
# for each key is also a list of length 2.Just like the first
# dictionary the first element in the list is the number of reviews
# that contain the word (key) and the second is the sum of all the
# review scores that contain the word (key).
def get_dictionaries(file_name):
    infile = open(file_name)
    words = {}
    num_words = {}
    for review in infile:
        # Getting the review, making it lowercase, splitting,
        # and then pushing words and scores into dictionary.
        new_review = review.lower().split()
        score = int(new_review[0])
        for word in new_review[1:]:
            dictionary_helper(words, word, score)
        dictionary_helper(num_words, str(len(new_review) - 1), score)
    return words, num_words        


# This function helps reduce redundancy and passes values
# to keys in a dictionary.
def dictionary_helper(dictionary, key, score):
    if key in dictionary:
        dictionary[key][0] += 1
        dictionary[key][1] += score
    # Initializing the key.
    else:
        dictionary[key] = [1, score]

        
# Returns the number of times a word is in a review.
def get_review_matches(infile, word):
    count = 0
    for review in infile:
        if word in review:
            count += 1
    return count


# Returns the sum of the scores with the reviews containing
# a specific word.
def get_review_sum(infile, word):
    total = 0
    for review in infile:
        if word in review:
            total += review[0]
    return total


# Ask the user for a key and show the statistics for that
# key if present in the given dictionary.
# The key entered by the user is converted to lower case.
def show_individual_stats(dictionary, prompt):
    original_word = input('Enter ' + prompt + ': ')
    new_word = original_word.lower()
    if new_word in dictionary:
        # Computing average ratings.
        average = get_average_rating(dictionary, new_word)
        print('Number of reviews =', dictionary[new_word][0])
        print('Average review score =', average)
    else:
        print(original_word, 'is not present in the dictionary.')
        

# Gets the average score for a dictionary.
def get_average_rating(dictionary, key):
    total = dictionary[key][1]
    amt_of_reviews = dictionary[key][0]
    if amt_of_reviews > 0:
        average = total / amt_of_reviews
    return average


# Ask the user if the want words above or below a given cutoff.
# Get the cutoff for average review score and the minimum number
# of reviews the word must appear in.
# Display the results.
def cutoff_stats(words_dictionary):
    print('Enter the letter a to show scores above a given cutoff,')
    user_input = input('anything else to show scores below a given cutoff: ')
    cut_off = eval(input('Enter the score cutoff between 0 and 4: '))
    min_reviews = eval(input('Enter the minimum number of reviews '
    + 'required: '))
    print('Results: ')
    if user_input == 'a':
        for key in words_dictionary:
            average = get_average_rating(words_dictionary, key)
            if (average >= cut_off) and (words_dictionary[key][0] >= min_reviews):
                print('word = ', key, '. Number of reviews = ',
                    words_dictionary[key][0],
                        '. Average review score = ', average, sep = '')
    else:
        for key in words_dictionary:
            average = get_average_rating(words_dictionary, key)
            if average <= cut_off and words_dictionary[key][0] >= min_reviews:
                average = get_average_rating(words_dictionary, key)
                print('word = ', key, '. Number of reviews = ',
                    words_dictionary[key][0],
                        '. Average review score = ', average, sep = '')
            

main()

