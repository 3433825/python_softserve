"""
    Converts a string x representing a number in the given base to an integer in decimal base
"""


def convert_any_to_int(x, base_num):
    return int(x, base=base_num)


x = "3f"
base_sys = 16
print(convert_any_to_int(x, base_sys))
