# Complete the solution so that it reverses all of the words within the string passed in.
# Example:
# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

def reverse_words(s):
    s1 = (s.split())
    s2 = list(reversed(s1))
    return ' '.join(s2)