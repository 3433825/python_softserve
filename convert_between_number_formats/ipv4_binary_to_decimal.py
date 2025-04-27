def binary_to_ipv4(binary_ip):
    binary_octets = binary_ip.split(".")
    decimal_octets = [str(int(octet, 2)) for octet in binary_octets]
    # return ".".join(decimal_octets)
    print()
    print(".".join(decimal_octets))
    print()


bin_ip = "11000000.10101000.01000000.00000000"
binary_to_ipv4(bin_ip)
# print(binary_to_ipv4(bin_ip))
