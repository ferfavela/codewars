# Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

# For example: (Input --> Output)

# 10 --> 1
# 99 --> 18
# -32 --> 5
# Let's assume that all numbers in the input will be integer values.

def sum_digits(number):
    if number < 0:
        number = number * -(1)
    string = str(number)
    listanova = [int(string) for string in string]
    return sum(listanova)