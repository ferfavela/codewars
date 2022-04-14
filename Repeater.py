# Write a function named repeater() that takes two arguments (a string and a number), and returns a new string where the input string is repeated that many times.

# Example: (Input1, Input2 --> Output)
# "a", 5 --> "aaaaa"

def repeater(string, n):
    aux = 0
    str = []
    while aux < n:
        aux +=1
        str.append(string)
    return ''.join(str)