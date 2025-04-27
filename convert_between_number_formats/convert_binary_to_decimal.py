"""
    Convert a string x representing a number in the binary base to an integer in decimal base
"""


def convert_binary_to_decimal(binary_number_string):
    return int(binary_number_string, base=2)


bin_number_str = "10001010"
print(convert_binary_to_decimal(bin_number_str))
