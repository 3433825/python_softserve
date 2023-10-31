"""
The reduce() function in Python is a part of the functools module. It applies a specified binary function cumulatively
to the items of an iterable, from left to right, so as to reduce the iterable to a single value.

The basic syntax of reduce() is:

functools.reduce(function, iterable[, initial])
"""
from functools import reduce
from Data import data

example_list = data.UNSORTED_NUMBERS_LIST
print(example_list)
result = reduce(lambda x, y: x + y, example_list)
print(result)

result = reduce(lambda x, y: x if (x > y) else y, example_list)
print(result)

def add(x, y):
    return x + y

result = reduce(add, example_list)
print(result)

def find_max(x, y):
    if x > y:
        max = x
    else:
        max = y
    return max

result = reduce(find_max, example_list)
print(result)
