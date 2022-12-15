# Title: Primes Program
# Program created by William Schaeffer
# CPS 313
# P. 428-429, Exercise 12, Primes Program
# 02.01.22

# This program will allow the user to enter a number. The program will display a list of all intgeters up to that number
    # and determine if each is a prime or composite number

# imports for functions

import primefunc

# Main Function

def main():
    
    # initialize user input variable and test to see if a positive integer
    positiveInteger = primefunc.integer_input()

    # create list with entered positive integer
    integer_list = primefunc.create_list(positiveInteger)

    # print list for testing purposes
    #print(f'{integer_list}')

    # test to see if each integer on created list is prime or composite
    primefunc.prime_er_no(integer_list)


# Function Definition

def welcome_function():                                 # function to welcome user

    print(f'Welcome to the Primes Program!\n\n')

main()                                                  # call main function

