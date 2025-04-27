def ipv4_decimal_to_binary(ip):
    octets = ip.split(".")
    binary_octets = [bin(int(octet))[2:].zfill(8) for octet in octets]
    return ".".join(binary_octets)


ipv4_dec = "172.16.98.250"
print(ipv4_decimal_to_binary(ipv4_dec))
