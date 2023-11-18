"""
Цей вид сортування вивчають на початку знайомства з дисципліною Computer Science, оскільки він максимально просто
демонструє саму концепцію сортування.
Цей підхід полягає у тому, що перебір здійснюється за списком і з порівнянням сусідніх елементів. Вони міняються
місцями в тому випадку, якщо порядок неправильний. І так триває до тих пір, поки всі елементи не розташуються в
потрібному порядку.
У бульбашкового сортування складність в гіршому випадку - O (n ^ 2), через велику кількість повторень.

This type of sorting is taught at the beginning of the Computer Science discipline because it demonstrates the
concept of sorting in the simplest way possible.
This approach is based on going through a list and comparing neighbouring elements. They are swapped if the order
is incorrect. And so it goes on until all the elements are in the right order. Bubble sorting has a worst-case
complexity of O(n ^ 2), due to the large number of repetitions.
"""
# import pytest

# def test_buble_sort(get_numbers_list):
#     numbers_list = get_numbers_list
#     print(numbers_list)
#     def swap(i, j):
#         numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]
#
#     n = len(numbers_list)
#     swapped = True
#
#     x = -1
#     while swapped:
#         swapped = False
#         x = x + 1
#         for i in range(1, n-x):
#             if numbers_list[i - 1] > numbers_list[i]:
#                 swap(i - 1, i)
#                 swapped = True
#                 print(numbers_list)
#     sorted_numbers_list = numbers_list
#     print(sorted_numbers_list)

# unsorted_numbers_list = get_unsorted_9_100_numbers_list()


def buble_sort(numbers_list):
    print(numbers_list)

    def swap(i, j):
        numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]

    n = len(numbers_list)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if numbers_list[i - 1] > numbers_list[i]:
                swap(i - 1, i)
                swapped = True
                print(numbers_list)
    sorted_numbers_list = numbers_list
    return sorted_numbers_list


# buble_sort(data.numbers_list)
# buble_sort(unsorted_numbers_list)
