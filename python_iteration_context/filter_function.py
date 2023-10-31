"""
The filter() function in Python is a built-in function that constructs an iterator from elements of an iterable for
which a function returns true.
The basic syntax of filter() is:
filter(function, iterable)
"""

from Data import data

# filter even numbers
example_list = data.UNSORTED_NUMBERS_LIST
even_numbers_list = list(filter(lambda x: x % 2 == 0, example_list))
print(example_list)
print(f"even numbers from list {even_numbers_list}")

# filter numbers > 3
numbers_over_3_list = list(filter(lambda x: x > 3, example_list))
print(example_list)
print(f"numbers > 3 = {numbers_over_3_list}")

# filter palindromes
example_list = data.WORDS
print(example_list)
palindromes = list(filter(lambda word: word == word[::-1], example_list))
print(palindromes)
