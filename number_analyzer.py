"""
IS 303 A04 - Jeremy Eldredge

Collects numbers and produces statistical analysis (mean, min, max, range, count above average)

Inputs:
- user name (str)
- list of numbers

Processes:
- validate and collect user's list of numbers
- import math
- calculate mean, mix, max, range, count above average (functions)

Outputs:
- user name
- list of numbers
- calculations
"""

# collect inputs
user_name = input("User name: ")


import math
import statistics

# functions and global variables
def get_positive_int(prompt):
    # asks user how many numbers are in their list and validates to ensure it is a positive whole number
    while True:
        try:
            number_of_numbers= int(input(prompt))
            if number_of_numbers <= 0:
                print("Please enter a positive number.")
            else:
                return number_of_numbers
        except ValueError:
            print("That is not a valid number. Please try again.")
    return number_of_numbers

def append_numbers(number_of_numbers):
    numbers = []
    for i in range(number_of_numbers):
        numbers.append(float(input(f"Enter number {i + 1}: ")))
    return numbers

def number_analysis(numbers):
    mean = statistics.mean(numbers)
    num_max = max(numbers)
    num_min = min(numbers)
    list_range = num_max - num_min
    for number in numbers:
        count_above_mean = 0
        if number > mean:
            count_above_mean += 1
    return mean, num_max, num_min, list_range, count_above_mean
    
    
num_numbers = get_positive_int("How many numbers would you like to enter? ")
numbers = append_numbers(num_numbers)
mean, num_max, num_min, list_range, count_above_mean = number_analysis(numbers)

print("=" * 30)
print("Numbers Report")
print("=" * 30)
print(f"Mean: {mean}")
print(f"Max: {num_max}")
print(f"Min: {num_min}")
print(f"Range: {list_range}")
print(f"Count above mean: {count_above_mean}")