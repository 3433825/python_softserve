"""
The enumerate() function in Python is a built-in function that adds a counter to an iterable and returns it in a form
of enumerate object, which is an iterator that produces tuples containing the index and the corresponding element of
the iterable. It provides an easy way to loop over both the index and the element of a sequence (e.g., list, tuple,
string, etc.).
The basic syntax of enumerate() is:
enumerate(iterable, start=0)
"""

from Data import data

example_list = data.LIST_SIMPLE
needed_fruit = 'banana'
print(example_list)
for index, fruit in enumerate(example_list):
    if fruit == needed_fruit:
        print(f"Needed fruit '{needed_fruit}' has index {index}")


