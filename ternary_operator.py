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

print(less_number)
# *********************************************************
"""
In this example, we are using a nested if-else to demonstrate ternary operator. If a and b are equal then we will
print a and b are equal and else if a>b then we will print a is greater than b otherwise b is greater than a.
"""

a, b = 10, 20

print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")

# **********************************************************

"""
In this example, we are using tuples to demonstrate ternary operator. We are using tuple for selecting an item and 
if [a < b] is true it return 1, so element with 1 index will print else if [a<b] is false it return 0, so element with 
0 index will print.
"""
# Python program to demonstrate ternary operator
a, b = 10, 20

print( (b, a) [a < b] )
