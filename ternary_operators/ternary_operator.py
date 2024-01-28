"""
Python Ternary Operator and its Benefits
The Python ternary operator determines if a condition is true or false and then returns the appropriate value in
accordance with the result. The ternary operator is useful in cases where we need to assign a value to a variable
based on a simple condition, and we want to keep our code more concise — all in just one line of code.
It’s particularly handy when you want to avoid writing multiple lines for a simple if-else situation.

Syntax of Ternary Operator in Python
Syntax: [on_true] if [expression] else [on_false]

expression: conditional_expression | lambda_expr
"""

# Simple Method to use ternary operator

# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
less_number = a if a < b else b
greater_number = a if a > b else b

print(f"From numbers {a}, {b} less_number {less_number}")
print(f"From numbers {a}, {b} greater_number {greater_number}")
# *********************************************************
"""
In this example, we are using a nested if-else to demonstrate ternary operator. If a and b are equal then we will
print a and b are equal and else if a>b then we will print a is greater than b otherwise b is greater than a.
"""

comparison_result = "Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a"
print(f"Comparison result {a} and {b} is {comparison_result}")
print()

# **********************************************************

"""
In this example, we are using tuples to demonstrate ternary operator. We are using tuple for selecting an item and 
if [a < b] is true it return 1, so element with 1 index will print else if [a<b] is false it return 0, so element with 
0 index will print.
"""
# Python program to demonstrate ternary operator

less_number = (b, a)[a < b]  # if true element[1] is returned
print(f"Ternary operator like this 'less_number = (b, a) [a < b]' returns less_number = {less_number}")

greater_number = (a, b)[a < b]  # if true element[1] is returned
print(f"Ternary operator like this 'greater_number = (a, b) [a < b]' returns greater_number = {greater_number}")
print()
# ***********************************************************************

"""
In this example, we are using Dictionary to demonstrate ternary operator and
if [a<b] is true it return value of True key, so value of True key will print else if [a<b] is false value of False key 
will print.
"""

less_number = {True: a, False: b} [a < b]
print("Ternary operator like this 'less_number = {True: a, False: b} [a < b]'" + " " +
      f"returns less_number = {less_number}")
greater_number = {True: a, False: b} [a > b]
print("Ternary operator like this 'greater_number = {True: a, False: b} [a > b]'" + " " +
      f"returns greater_number = {greater_number}")
print()

# ******************************************************************

print((lambda: b, lambda: a)[a < b]())  # if true element[1] is returned

print((lambda: b, lambda: a)[a > b]())  # if false element[0] is returned
