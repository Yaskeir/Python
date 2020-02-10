#Mateusz Fido

import os, timeit
from fibonacci import exec_time

def symmetricDifference():
    '''Prints out the missing number using Set implementation.'''
    with open('99_numbers.txt', 'r') as numbers:
        numbers_list = []
        for number in numbers.readlines():
            numbers_list.append(int(number))
        print(set(numbers_list)^set(range(1,101)), "is missing!")

print("And it took", exec_time(symmetricDifference), "seconds to complete using the set method.")

def doubleForLoop():
    '''Prints out the missing number using two for loops, iterating 
    over the file and a sequence of natural numbers from 1 to 100.'''
    with open('99_numbers.txt', 'r') as numbers:
        checklist = [i for i in range(1,101)]
        numbers_list = []
        for number in numbers.readlines():
            numbers_list.append(int(number))
        for checker in checklist:
            if checker not in numbers_list:
                print(checker, "is missing!")

print("And it took", exec_time(doubleForLoop), "seconds to complete using two for loops.")

def listComprehension():
    '''Prints out the missing number using the same method as 
    the function above, only sped up using list comprehension.'''
    with open('99_numbers.txt', 'r') as numbers:
        checklist = [i for i in range(1,101)]
        numbers_list = []
        for number in numbers.readlines():
            numbers_list.append(int(number))
        missing = [j for j in checklist if j not in numbers_list]
        print(missing, "is missing!")

print("And it took", exec_time(listComprehension), "seconds to complete using list comprehension.")

def numberSum():
    '''Prints out the missing number using a hard-coded sum for numbers
    from 1 to 100 and subtracting the sum of numbers in the file, the
    difference being the wanted number.'''
    with open('99_numbers.txt', 'r') as numbers:
        sum_of_1_to_100 = 5050
        sum_of_99_numbers = 0
        for number in numbers.readlines():
            sum_of_99_numbers += int(number)
        difference = sum_of_1_to_100 - sum_of_99_numbers
        print(difference, "is missing!")

print("And it took", exec_time(numberSum), "seconds to complete using the summing method.")
