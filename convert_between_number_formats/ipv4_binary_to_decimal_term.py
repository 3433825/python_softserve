#!/usr/bin/env python3

import sys


def binary_to_ipv4(binary_ip):
    binary_octets = binary_ip.split(".")
    decimal_octets = [str(int(octet, 2)) for octet in binary_octets]
    # return ".".join(decimal_octets)
    print()
    print(".".join(decimal_octets))
    print()


# bin_ip = "11111111.11111111.11111110.00000000"
# binary_to_ipv4(bin_ip)
# print(binary_to_ipv4(bin_ip))

if __name__ == "__main__":
    binary_ip_value = sys.argv[1]
    binary_to_ipv4(binary_ip_value)
