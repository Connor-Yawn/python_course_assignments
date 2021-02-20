"""
Program: validation_with_try.py
Author: Connor Yawn
Last date modified: 02/19/2021

The purpose of this program is to grab first name, last name, age, and test scores one through --
three to find an average and return it to the user. It needs to take inputs and try-except
functions and give a statement telling the user what the issue was with their input.

"""
# Declarations
last_name = input("Please enter your last name:")
first_name = input("Please enter your first name:")
age = int(input("Please enter your age:"))
AMOUNT_OF_TESTS = 3
user_test1 = 0.0
user_test2 = 0.0
user_test3 = 0.0
test_average = 0
# =====================================================================================================================
try:
    test_one = "What was the score of your first test(Up to two decimal places)?"
    user_test1 = float(input(test_one))
except (TypeError, Exception):
    print("Error. Must be a float value.")
else:
    if user_test1 < 0:
        print("Negative score found in test 1. Cannot calculate average with a negative value. Please try again.")
finally:
    print("This has been added for Test 1.")
# ======================================================================================================================
try:
    test_two = "What was the score of your second test(Up to two decimal places)?"
    user_test2 = float(input(test_two))
except (TypeError, Exception):
    print("Error. Must be a float value")
else:
    if user_test2 < 0:
        print("Negative score found in test 2. Cannot calculate average with a negative value. Please try again.")
finally:
    print("This has been added for Test 2.")
# ======================================================================================================================
try:
    test_three = "What was the score of your third test(Up to two decimal places)?"
    user_test3 = float(input(test_three))
except (TypeError, Exception):
    print("Error. Must be a float value.")
else:
    if user_test3 < 0:
        print("Negative score found in test 3. Cannot calculate average with a negative value. Please try again.")
finally:
    print("This has been added for Test 3")
test_average += user_test1
test_average += user_test2
test_average += user_test3

test_averages = (test_average/AMOUNT_OF_TESTS)
test_averages = "{:.2f}".format(test_averages)
if user_test1 > 0 and user_test2 > 0 and user_test3 > 0:
    print(f'{last_name}, {first_name} age: {age} Average Grade: {test_averages}')
else:
    print("Try again with non-negative values.")

"""
I worked on this program for awhile and I ran into 50 different issues. It's still not bulletproof, but I think it is good. 
I think I used the try-except values correctly to catch non-float/integer values and keep the program running without any hard stops.
         INPUTS                            EXPECTED OUTPUT                                       ACTUAL OUTPUT
     -100/-100/100                    Try again with non negative values.                           -33.33
# I added the if statement with all unit tests being false below 0.
     100/100/h                       Try again with non-negative values.                          ERROR CODE- blew up my code
# I changed the whole format of my code to get rid of useless variables and force my program to work with the TypeError
and add it to my code with (This has been added for test ..) and then give the error message to the user versus my code crashing.
     100/100/-100                     Negative score found in test 3                    Negative score found in test 3  
# The same format used for my first try-except-else with the others, and it worked correctly. 
    100/-97.98/100                        Negative score found in test 2                    Negative score found in test 2      
# It worked for the second test as well. It works with numbers and float values.    
"""
