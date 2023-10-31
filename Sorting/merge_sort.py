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

