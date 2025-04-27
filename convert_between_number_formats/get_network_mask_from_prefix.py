import ipaddress


def get_subnet_mask(prefix):
    # Створюємо об'єкт IPv4Network з префікса підмережі
    network = ipaddress.IPv4Network(f"0.0.0.0{prefix}", strict=False)

    # Отримуємо маску підмережі у вигляді рядка
    subnet_mask = str(network.netmask)

    return subnet_mask


# Приклад використання
prefix = "/24"
subnet_mask = get_subnet_mask(prefix)
print(f"Маска підмережі для префікса {prefix}: {subnet_mask}")
