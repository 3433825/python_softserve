def is_all_uppercase(input_string):
    # Check if the string is empty or has no letters
    if not input_string or not any(char.isalpha() for char in input_string):
        return True

    # Check if all alphabetic characters are in uppercase
    return all(char.isupper() or not char.isalpha() for char in input_string)


upper_string = "UPPER STRING"
print(is_all_uppercase(upper_string))
