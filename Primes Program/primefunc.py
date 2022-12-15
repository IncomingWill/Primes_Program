# Title: Primes Program, Functions
# Program created by William Schaeffer
# CPS 313
# P. 428-429, Exercise 12, Primes Program
# 02.01.22

# imports for command-line args and to make math easy

import sys   
from math import sqrt 

# Function definitions for Primes Program

# Function to test if input is a proper integer
    # Commented out sections are for user input

def integer_input():
    while True:
        try:
            #n = int(input('Please enter a positive integer: '))        # user input
            n = int(sys.argv[1])                                        # command-line argument input
            while n < 1:
                n = int(input('Please enter a positive integer: '))
                return n
            return n
        except ValueError as error:
            print(f'{error} is not valid input. Please try again: ')

# Fuction to create number list based on user input
    # Initialize list of numbers, append each number to list from 2 to user input + 1

def create_list(n):

    number_list = []                                    # initialize list of numbers, to be defined by user

    for i in range(2, n + 1, 1):                        # append each integer to number list from 2 to user input + 1
        number_list.append(i)                           
    
    return number_list                                  # return created number list to main function


# Function to determine if each number on the created list is prime or composite
    # Function will print each number in the list
        # For each number on the list, function will perform arithmetic to determine prime or composite

def prime_er_no(list):
                                                   
    for number in list:
        print(number, end = '')
        flag = 0                                        # set flag for prime (0) or not(1)
        for i in range(2, int(sqrt(number)) + 1):       # range starts at 2, stops at sqrt of user input + 1
            if (number % i == 0):                       # if there is no remainder, input is even or can be squared and cannot be prime 
                flag = 1
                break
        if (flag == 0):
            print(f' is prime time')
        else:
            print(f' is composite')
