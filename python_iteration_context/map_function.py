"""
Add to every element 10

The map() function in Python is a built-in function that allows you to apply a specified function to all the
items in an input list (or any iterable) and returns an iterator of the results. It takes two arguments:
the function to be applied and the iterable.
The basic syntax of map() is:
map(function, iterable)
for instance:

"""

from Data import data


def add_10(x):
    x += 10
    return x

print(data.UNSORTED_NUMBERS_LIST)
added_10 = list(map(lambda x: x + 10, data.UNSORTED_NUMBERS_LIST))
print(added_10)

print(data.UNSORTED_NUMBERS_LIST)
add_10_new = list(map(add_10, data.UNSORTED_NUMBERS_LIST))
print(add_10_new)
