from modules import advanced_logg

logger = advanced_logg.advanced_logger()


class SortMethods:
    def __init__(self, array):
        self.unsorted_numbers_list = array

    def buble_sort(self):
        """
        Sorts operations_with_numbers list in ascending order
        """
        numbers_list = self.unsorted_numbers_list
        def swap(i, j):
            numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]

        n = len(numbers_list)
        swapped = True

        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n - x):
                if numbers_list[i - 1] > numbers_list[i]:
                    swap(i - 1, i)
                    swapped = True
        sorted_numbers_list = numbers_list
        logger.info("Generated list is sorted by buble method in ascending order")
        return sorted_numbers_list
