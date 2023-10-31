from Data import data
from Sorting import turing


def test_sorting_least_repeated():
    list_before_sorting = data.K
    list_after_sorting = turing.sort_least_repeated(list_before_sorting)
    etalon = data.K_AFTER_SORTING_LEAST_REPEATED
    assert list_after_sorting == etalon
