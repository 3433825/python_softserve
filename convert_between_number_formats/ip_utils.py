import ipaddress


class IPUtils:
    def __init__(
        self, host_ip=None, subnet_mask=None, host_addresses=None, prefix=None
    ):
        self.host_ip = host_ip
        self.subnet_mask = subnet_mask
        self.host_addresses = host_addresses
        self.prefix = prefix

    def get_network_address(self):
        """
        Method receives host address with subnet mask as prefix and returns network address
        Use example:
        # Створюємо екземпляр класу IPUtils
        ip_utils = IPUtils(ip_address="192.168.1.100/24")
        # Викликаємо метод get_network_address()
        network_address = ip_utils.get_network_address()
        # Виводимо результат
        print(f"Network Address: {network_address}")
        """

        if "/" in self.host_ip:  # Якщо вхідний рядок містить префікс підмережі
            # Розділити адресу та префікс підмережі
            ip, prefix = self.host_ip.split("/")
            # Повернути адресу мережі
            return str(
                ipaddress.IPv4Network(f"{ip}/{prefix}", strict=False).network_address
            )
        else:
            # Якщо вказана окрема маска підмережі
            if self.subnet_mask:
                # ip_address = ipaddress.ip_address(self.host_ip)
                # Побудувати об'єкт підмережі з вказаною маскою
                network = ipaddress.IPv4Network(
                    f"{self.host_ip}/{self.subnet_mask}", strict=False
                )
                # Повернути адресу мережі
                return str(network.network_address)
            else:
                return "Не вказана маска підмережі"

    def get_network_addresses(self):
        """
        Method receives list host addresses with subnet prefixes and returns dictionary with
        network addresses as keys and lists of host addresses belonging to them as values.
        Use example:
        ip_utils_3 = IPUtils(host_addresses=["172.16.98.250/23", "192.168.1.100/24", "10.0.0.5/8"])
        network_addresses_dict = ip_utils_3.get_network_addresses()
        for network, hosts in network_addresses.items():
            print((network, hosts))
        """

        network_addresses = {}
        for host in self.host_addresses:
            if "/" in host:
                ip, subnet_mask = host.split("/")
                network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)
                network_address = str(network.network_address)
                if network_address in network_addresses:
                    network_addresses[network_address].append(host)
                else:
                    network_addresses[network_address] = [host]
            else:
                continue
        return network_addresses

    def get_subnet_mask(self):
        """ """
        network = ipaddress.IPv4Network(f"0.0.0.0{self.prefix}", strict=False)
        return str(network.netmask)

    def get_subnet_range(self):
        interface = ipaddress.IPv4Interface(f"{self.host_ip}/{self.subnet_mask}")
        network = interface.network
        broadcast_address = network.broadcast_address
        subnet_range = f"{network.network_address} - {broadcast_address}"
        return subnet_range

    def get_subnet_range_from_host_address(self):
        ip, subnet_mask = self.ip_address.split("/")
        interface = ipaddress.IPv4Interface(f"{ip}/{subnet_mask}")
        network = interface.network
        broadcast_address = network.broadcast_address
        subnet_range = f"{network.network_address} - {broadcast_address}"
        return subnet_range


# # Приклади використання

# # Створюємо екземпляр класу IPUtils
# # Викликаємо метод get_network_address()
# # Виводимо результат

# ip_utils = IPUtils(ip_address="192.168.1.100/24")
# network_address = ip_utils.get_network_address()
# print(f"Network Address: {network_address}")

# ip_utils = IPUtils(host_ip="192.168.1.168", subnet_mask="255.255.255.0")
# network_address = ip_utils.get_network_address()
# print(f"Network Address: {network_address}")

# ip_utils = IPUtils(host_ip="192.168.1.168")
# network_address = ip_utils.get_network_address()
# print(f"Network Address: {network_address}")

ip_utils = IPUtils(
    host_addresses=[
        "192.168.10.2/24",
        "192.167.10.74/24",
        "193.168.10.16/24",
        "192.168.10.56/24",
        "192.168.100.62",
    ]
)
networks = ip_utils.get_network_addresses()
# print(network_addresses)
for network_ip, hosts in networks.items():
    print((network_ip, hosts))

# ip_utils = IPUtils(ip_address="192.168.1.100")
# ip_utils = IPUtils(host_addresses=["172.16.98.250/23", "192.168.1.100/24", "10.0.0.5/8"])
# network_addresses_dict = ip_utils_3.get_network_addresses()
# print(network_addresses_dict)
#
# ip_utils_2 = IPUtils("172.16.98.250", "255.255.254.0")
# subnet_range_from_host = ip_utils_2.get_subnet_range_from_host_address()
# print(f"Subnet Range from Host Address: {subnet_range_from_host}")
#

#
# ip_utils_4 = IPUtils(prefix="/28")
# subnet_mask = ip_utils_4.get_subnet_mask()
# print(f"Subnet Mask for Prefix {ip_utils_4.prefix}: {subnet_mask}")

# ip_utils_1 = IPUtils("192.168.1.100", "255.255.255.0")
# network_address = ip_utils_1.get_network_address()
# subnet_range = ip_utils_1.get_subnet_range()
# print(f"Network Address: {network_address}")
# print(f"Subnet Range: {subnet_range}")
