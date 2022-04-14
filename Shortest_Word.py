# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(s):
    lista = s.split(' ')
    lista1 = min(lista, key=lambda x: len(x.strip()))
    return len(lista1)