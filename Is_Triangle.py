# Implement a function that accepts 3 integer values a, b, c. 
# The function should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

def is_triangle(a, b, c):
    if a >= b and a >= c:
        return b+c>a
    if b >= c and b >= a:
        return c+a>b
    if c >= a and c >= b:
        return b+a >c