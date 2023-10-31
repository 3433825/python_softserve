import pytest
import random


@pytest.fixture()
def get_unsorted_numbers_list():
    unsorted_numbers_list = random.sample(range(20), 9)
    yield unsorted_numbers_list
