"""
Сортування вставками швидке і просте. На кожній ітерації програма бере один з елементів і підшукує для нього місце у
вже відсортованому списку. Так відбувається до тих пір, поки не залишиться жодного невикористаного елемента.

Insertion sorting is quick and easy. At each iteration, the programme takes one of the items and searches for a place
for it in the already sorted list. This happens until there are no unused items left.
"""
from Data import data


def insertion_sort(get_unsorted_numbers_list):
    for i in range(len(arr)):
        initial_array = arr
        current_value = arr[i]
        position = i

        while position > 0 and arr[position - 1] > current_value:
            # rearrange the numbers_operations, moving down the list
            arr[position] = arr[position - 1]
            position = position - 1

        arr[position] = current_value

    return arr


arr_l = data.UNSORTED_NUMBERS_LIST
print(arr_l)
print(insertion_sort(arr_l))
