# File: strings.py
# Description: Implements three functions that use
# and manipulate strings.
# Assignment Number: 8
#
# Name: Matthew Molinar
# EID:  mam24689
# Email: molinar@utexas.edu
# Grader: Skyler
#
# On my honor, Matthew Molinar, this programming assignment is my own
# work and I have not provided this code to any other student. 


# s1 and s2 shall be strings. This function returns the number of chars
# in s1 and s2 that match based on position.
def num_chars_same(s1, s2):
    total = 0
    # Checking the indices of each string, for matches.
    for i in range(0,len(s1)):
        for j in range(0,len(s2)):
            if s1[i] == s2[j] and i == j:
                total += 1
    return total
        

# s1 shall be a string and num shall be an integer >= 0.
# The function returns a stretched version of s1 with each
# character repeated. The number of repitions is num times
# the position of that character if we were to use 1 based indexing. 
def stretch(s1, num):
    stretch_str = ''
    # Creating new string content for each index.
    for i in range(0,len(s1)):
        stretch_str += num * (i + 1) * s1[i]
    return stretch_str


# s1 and s2 shall be strings.
# The method returns the number of characters at the end of
# s1 and s2 that match. Stops at the first mistmatched character.
def length_of_matching_suffix(s1, s2):
    total = 0
    second_string_iterator = len(s2) - 1
    # Checks the indices from the back, in a backwards fashion.
    for first_string_iterator in range(len(s1) - 1, 0 - 1, -1):

        # Stops the search if strings are not the same.
        if s1[first_string_iterator] == s2[second_string_iterator]:
            total += 1
        else:
            break
        second_string_iterator -= 1
    return total


# Run tests on the functions. Ask the user for input.
def main():
    num_tests = eval(input('Enter the number of tests per method: '))
    print('Testing num chars same function.')
    test_functions_with_two_string_parameters(num_tests, num_chars_same)
    print('Testing stretch function.')
    stretch_tests(num_tests)
    print('Testing length of matching suffix function.')
    test_functions_with_two_string_parameters(num_tests,
                                              length_of_matching_suffix)


# Test the functions that take 2 String parameters.
def test_functions_with_two_string_parameters(num_tests, function_to_test):
    for i in range(0, num_tests):
        s1 = input('Enter first string: ')
        s2 = input('Enter second string: ')
        print(function_to_test(s1, s2))
    print()


# Test the stretch function.
def stretch_tests(num_tests):
    for i in range(0, num_tests):
        s1 = input('Enter the string: ')
        num = eval(input('Enter number of times to repeat: '))
        print(stretch(s1, num))
    print()
    
            
main()