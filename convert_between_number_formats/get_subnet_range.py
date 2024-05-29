import ipaddress


def get_subnet_range(ip_address, subnet_mask):
    # Створюємо об'єкт IPv4Interface з IP-адреси та маски підмережі
    interface = ipaddress.IPv4Interface(f"{ip_address}/{subnet_mask}")

    # Отримуємо мережеву адресу та broadcast-адресу підмережі
    network = interface.network
    broadcast_address = network.broadcast_address

    # Формуємо та повертаємо діапазон адрес підмережі
    subnet_range = f"{network.network_address} - {broadcast_address}"
    return subnet_range


# Приклад використання
ip_address = "192.168.1.100"
subnet_mask = "255.255.255.0"

subnet_range = get_subnet_range(ip_address, subnet_mask)
print(f"Діапазон адрес підмережі: {subnet_range}")
