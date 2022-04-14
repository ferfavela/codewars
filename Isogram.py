# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)

def is_isogram(string):
    iso = string.lower()
    iso1 = set(iso)
    iso2 = sorted(iso1)
    iso3 = sorted(iso)
    if iso2 == iso3:
        return True
    else:
        return False