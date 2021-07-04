# File: movies.py
# Description: A program works with movie ratings and reviews.
# Based on the Nifty Assignment:
# http://nifty.stanford.edu/2016/manley-urness-movie-review-sentiment/
# Assignment Number: 12
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
    print('Welcome to the movie sentiment program.')
    print('Enter a word to see the average rating of movies with that word.')
    file_name = input('Enter file name with reviews: ')
    reviews = get_reviews(file_name)
    choice = get_choice()
    # List of our functions. They all take a single parameter, the reviews.
    functions = [print_word_sentiment, print_sentiments_from_file,
                 print_longest_review, print_shortest_review]
    VALUE_1 = ord('1')
    while '1' <= choice <= '4':
        # Get the index of the function to call.
        index = ord(choice) - VALUE_1
        function = functions[index](reviews)
        choice = get_choice()

    
# Display the menu and get the users choice.
# Returns the user's choice as a String.
def get_choice():
    print()
    print('OPTIONS:')
    print('1. See average rating for a word.')
    print('2. Show average reviews for all words in a file.')
    print('3. See the longest review.')
    print('4. See the shortest review.')
    result = input('Please enter your choice: ')
    print()
    return result


# Given the file name, create a list of lists with the movie reviews.
# We expect one review per line. The first element will be an int [0, 4].
# The rest of the line shall be the review.
# All letters in the reviews are converted to lower case.
def get_reviews(file_name):
    reviews = []
    infile = open(file_name)
    get_lines(infile, reviews)
    return reviews


# I'm getting the line and turning it into a list, then returning it.
def get_lines(infile, reviews):
    for line in infile:
        line = line.lower()
        line_words = line.split()
        reviews.append(line_words)


# Get a word from the user and determine the average rating of
# reviews that contain that word. reviews is a list of lists that
# contain the reviews.
def print_word_sentiment(reviews):
    word = input('Enter the word to search for: ')
    get_average_sentiment(reviews, word)            
   

# Totals the ratings for words in reviews, and retun the average
# and how many times the word appeared.       
def get_average_sentiment(reviews, word):
    new_word = word.lower().strip()
    review_count = 0
    total_rating = 0
    for review in reviews:
        if new_word in review[1:]:
            total_rating += int(review[0])
            review_count += 1
    # Displaying number of reviews, and average if above zero.
    if review_count > 0:
        str_modify = 'reviews.'
        average = total_rating / review_count
        if review_count == 1:
            str_modify = 'review.'
        print(word, 'appeared in', review_count, str_modify,
            'Average review score =', average)
    else:
        print(word, 'did not appear in any reviews')

    
# Ask the user for the name of a file with words and phrases.
# We assume one word or phrase per line in the file.
# For each word or phrase in the file, determine and show
# the average rating of reviews that contain the given word.
def print_sentiments_from_file(reviews):
    file_name = input('Enter file name with words to check: ')
    infile = open(file_name)
    count = 0
    for word in infile:
        count += 1
        word = word.strip()
        print('Word number ', count, ' is \'', word, '\'. Results: ', sep = '')
        get_average_sentiment(reviews, word)
        print()
        
    
# Print information about the longest review.
def print_longest_review(reviews):
    longest_review = []
    maxi = 0
    for review in reviews:
        count = get_count(review)
        if count > maxi:
            maxi = count
            longest_review = review[1:]
    print('Longest review has', maxi, 'words.')
    print('Review as list:', longest_review)
            

# Goes through each review and returns how many words are in it.   
def get_count(review):
    count = 0
    review = review[1:]
    for word in review:
        count += 1
    return count


# Print information about the longest review.
def print_shortest_review(reviews):
    shortest_review = []
    mini = len(reviews[0][1:])
    for review in reviews:
        count = get_count(review)
        if count < mini:
            mini = count
            shortest_review = review[1:]
    print('Shortest review has', mini, 'words.')
    print('Review as list:', shortest_review)


main()