# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

# https://www.codewars.com/kata/576bb71bbbcf0951d5000044

def count_positives_sum_negatives(arr):
    if arr == []:
        return arr
    soma, conta = 0, 0
    for each in arr:
        if each < 0:
            soma = each + soma
        if each > 0:
            conta = conta + 1
    return [conta, soma]