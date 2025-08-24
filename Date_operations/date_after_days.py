from datetime import datetime, timedelta


def get_date_after_days(base_date: str, days: int) -> str:
    """
    Повертає дату через вказану кількість днів від заданої дати.

    Args:
        base_date (str): Початкова дата у форматі 'YYYY-MM-DD' (наприклад, '2025-06-13')
        days (int): Кількість днів для додавання (може бути від'ємним)

    Returns:
        str: Нова дата у форматі 'YYYY-MM-DD'

    Raises:
        ValueError: Якщо формат дати неправильний або days не є числом
    """
    try:
        # Перетворюємо рядок дати у об'єкт datetime
        date_obj = datetime.strptime(base_date, "%d-%m-%Y")

        # Додаємо вказану кількість днів
        new_date = date_obj + timedelta(days=days)

        # Повертаємо дату у тому ж форматі
        return new_date.strftime("%d-%m-%Y")
    except ValueError as e:
        raise ValueError("Неправильний формат дати (очікується 'DD-MM-YYYY') або days не є числом") from e


# Приклад використання
if __name__ == "__main__":
    # Поточна дата: 13 червня 2025 року
    base_date = "19-05-2025"
    print(get_date_after_days(base_date, 70))