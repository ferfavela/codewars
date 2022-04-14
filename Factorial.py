# Your task is to write function factorial.

def factorial(n):
    if n == 0:
        return 1
    for i in range(1, n):
        n = i * n
    return n