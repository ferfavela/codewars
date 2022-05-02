# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# Examples (a, b) --> output (explanation)
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

# https://www.codewars.com/kata/55f2b110f61eb01779000053

def get_sum(a,b):
    if a > b:
        a, b = b, a
        b = b+1
        return sum(list(range(a,b)))
    else:
        b = b+1
        return sum(list(range(a,b)))