from Data import data
from string import punctuation

def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1


sequence = data.SUBTITLE.lower().split()
sequence = list(map(lambda word: word.strip(punctuation), sequence))

print(linear_search(sequence, "zenity"))