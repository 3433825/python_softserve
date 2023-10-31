"""
Сортування вибором також доволі простий алгоритм, але більш ефективний у порівнянні з бульбашковим сортуванням.
У цьому алгоритмі список (або масив) ділиться на дві частини: список з відсортованими елементами та список з
елементами, які потрібно відсортувати. Спочатку шукається найменший елемент у другому списку. Він додається в кінець
першого. Таким чином алгоритм поступово формує список від меншого до більшого. Так відбувається до тих пір, поки не
 буде готовий відсортований масив.

Selection sort is also a fairly simple algorithm, but it is more efficient than bubble sort.
In this algorithm, a list (or array) is divided into two parts: a list with sorted items and a list with items to be
sorted. First, the smallest element in the second list is found. It is added to the end of the first one. In this way,
the algorithm gradually builds the list from smaller to larger. This happens until the sorted array is ready.
"""
from Data import data


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            # choose min value
            if arr[j] < arr[min_index]:
                min_index = j

        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr


arr_l = data.UNSORTED_NUMBERS_LIST
print(arr_l)
print(selection_sort(arr_l))
