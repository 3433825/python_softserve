import pytest
import random
from modules import advanced_logg

logger = advanced_logg.advanced_logger()


@pytest.fixture()
def get_unsorted_9_100_numbers_list():
    """
    generates random 9-numbers list with range = 100
    """
    unsorted_numbers_list = random.sample(range(100), 9)
    logger.info(f"Generated random 9-numbers list {unsorted_numbers_list} ")
    yield unsorted_numbers_list
