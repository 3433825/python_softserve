"""
The zip() function in Python is a built-in function that takes one or more iterables (like lists, tuples, etc.) and
aggregates their elements element-wise, creating an iterator of tuples. Each tuple contains the elements at the same
position from each of the input iterables.

The basic syntax of zip() is:
zip(*iterables)
iterables: One or more iterable objects to be zipped together.
Here's an example to demonstrate how zip() works:
names = ['John', 'Jane', 'Jim']
scores = [85, 90, 75]

# Combine names and scores element-wise
zipped_data = zip(names, scores)

# Convert the result to a list (since zip returns an iterator)
zipped_data_list = list(zipped_data)
"""

from Data import data

names = data.NAMES
names.append('Alex')
scores = data.SCORES
# scores.append(80)
grade = data.GRADES

print(names)
print(scores)
print(grade)
print()

zip_result = zip(names, scores, grade)
print(list(zip_result))
print()
zip_dict_result = dict(zip(names, scores))
print(zip_dict_result)
