#!/usr/bin/env python3


def convert_decimal_to_binary():
    # return bin(decimal_n)[2:]
    keep_going = "y"
    while keep_going == "y":
        dec_number = int(input("Decimal number: "))
        bin_number = bin(dec_number)[2:]
        print()
        print(f"Decimal number: {dec_number}")
        # print()
        print(f" Binary number: {bin_number}")
        print()
        keep_going = input('Continue "y", exit "n":')


if __name__ == "__main__":
    convert_decimal_to_binary()
# dec_number = input("Decimal number: ")
# print(convert_decimal_to_binary(dec_number))
# convert_decimal_to_binary()
