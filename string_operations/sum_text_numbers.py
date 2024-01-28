import re


def sum_text_numbers(text):
    # Use regular expression to find all numbers in the text
    # Convert the list of strings to a list of integers and calculate the sum
    return sum(map(int, re.findall(r"\b\d+\b", text)))


example_string = "This is the 1st string with numbers 2 and 11"
print(sum_text_numbers(example_string))


def sum_text_numbers_filter(text: str) -> int:
    return sum(map(int, filter(str.isdigit, text.split())))


print(sum_text_numbers_filter(example_string))
