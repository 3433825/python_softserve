import ipaddress


def get_network_address(host_address):
    # Розділяємо адресу хоста та маску підмережі
    ip, subnet_mask = host_address.split("/")

    # Створюємо об'єкт IPv4Network з адреси хоста та маски підмережі
    network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)

    # Повертаємо адресу мережі
    return str(network.network_address)


# Приклад використання
host_address = "172.16.98.250/23"
network_address = get_network_address(host_address)
print(f"Адреса мережі: {network_address}")
