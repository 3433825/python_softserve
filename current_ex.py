# def sequence(low, high):
#     # Complete the outer loop range to make the loop run twice
#     # to create two rows
#     for x in range(1, 3):
#         # Complete the inner loop range to print the given variable
#         # numbers starting from "high" to "low"
#         # Hint: To decrement a range parameter, use negative numbers
#         for y in range(high, low - 1, -1):
#             if y == low:
#                 # Don’t print a comma after the last item
#                 print(str(y))
#             else:
#                 # Print a comma and a space between numbers
#                 print(str(y), end=", ")
#
# sequence(1, 3)
# # Should print the sequence 3, 2, 1 two times, as shown above.

# *****************************************************************************
# def counter(start, stop):
#     value = start
#     return_string = ""
#     if start > stop:
#         return_string = "Counting down: "
#         while value >= stop: # Complete the while loop
#             return_string += str(value) # Add the numbers to the "return_string"
#             if value > stop:
#                 return_string += ","
#             value -= 1 # Increment the appropriate variable
#     else:
#         return_string = "Counting up: "
#         while value <= stop: # Complete the while loop
#             return_string += str(value) # Add the numbers to the "return_string"
#             if value < stop:
#                 return_string += ","
#             value += 1 # Increment the appropriate variable
#     return return_string
#
# counter(2, 8)

# ***************************************************************************

def even_numbers(maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all even numbers
    # up to and including the "maximum" value, but excluding 0.
    for number in range(2, maximum + 1, 2):
        return_string += str(number) + " "

        # Complete the body of the loop by appending the even number
        # followed by a space to the "return_string" variable.
        #___

    # This .strip command will remove the final " " space at the end of
    # the "return_string".
    return return_string.strip() 

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

