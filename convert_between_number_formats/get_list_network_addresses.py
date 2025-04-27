import ipaddress


def get_network_addresses(host_addresses):
    network_addresses = {}

    for host_address in host_addresses:
        # Розділяємо адресу хоста та маску підмережі
        ip, subnet_mask = host_address.split("/")

        # Створюємо об'єкт IPv4Network з адреси хоста та маски підмережі
        network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)

        # Додаємо адресу хоста та адресу мережі до словника
        network_addresses[host_address] = str(network.network_address)

    return network_addresses


# Приклад використання
host_addresses = [
    "192.168.10.2/24",
    "192.167.10.74/24",
    "193.168.10.16/24",
    "192.168.10.56/24",
    "192.168.100.62/24",
]
network_addresses_dict = get_network_addresses(host_addresses)
# print(network_addresses_dict)

# Виводимо словник в консоль
for host_address, network_address in network_addresses_dict.items():
    print(f"{host_address} - {network_address}")
