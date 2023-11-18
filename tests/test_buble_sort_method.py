import pytest

from modules import advanced_logg
from Sorting.sort_numbers import SortMethods


logger = advanced_logg.advanced_logger()


@pytest.fixture()
def setup_teardown(get_unsorted_9_100_numbers_list):
    numbers_list = get_unsorted_9_100_numbers_list
    sort_methods = SortMethods(numbers_list)
    yield sort_methods


def test_buble_sort_method(setup_teardown):
    logger.info("Verify that buble sort method sorts numbers list properly")
    sort_methods = setup_teardown
    sorted_list = sort_methods.buble_sort()
    assert sorted_list[0] < sorted_list[1] < sorted_list[2]