def count_trailing_zeros(number):
    # Convert the number to a string
    number_str = str(number)

    # Use rstrip to remove trailing zeros and count the length

    return len(number_str) - len(number_str.rstrip("0"))


print(count_trailing_zeros(1000))
