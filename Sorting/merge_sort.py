"""
Сортування злиттям складається з двох етапів:
Невідсортований список послідовно ділиться на N списків, де кожен включає один «невідсортований» елемент,
а N — це число елементів в оригінальному масиві.
Списки послідовно зливаються групами по два, створюючи нові відсортовані списки до тих пір, поки не з'явиться
один фінальний відсортований список.

Merge sorting includes two steps:
The unsorted list is sequentially divided into N lists, where each list includes one "unsorted" element, and N is the
number of elements in the original array.
The lists are successively merged in groups of two, creating new sorted lists until one final sorted list appears.
"""

from Data import data


def merge_sort(arr):
    # dividing array
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # perform merge_sort recursively on both sides
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    print(left)
    print(right)

    # merge the sorted halves
    return merge(left, right, arr.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        # sort each one and put it into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


arr_l = data.UNSORTED_NUMBERS_LIST
print(arr_l)
print(merge_sort(arr_l))

