import pytest
import random
import logging
from datetime import datetime
from modules import advanced_logg


@pytest.fixture
def get_logger(path="./{:%Y-%m-%d}.log"):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt=f"[%(asctime)s] %(levelname)s %(filename)s %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
    )

    # file_handler = logging.FileHandler(
    #     '../logs/{:%Y-%m-%d}.log'.format(datetime.now()),
    #     mode='a'
    # )

    file_handler = logging.FileHandler(path.format(datetime.now()), mode="a")

    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # stream_handler = logging.StreamHandler()
    # stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    # logger.addHandler(stream_handler)

    return logger


@pytest.fixture
def get_unsorted_9_100_numbers_list(get_logger):
    """
    generates random 9-numbers_operations list with range = 100
    """
    unsorted_numbers_list = random.sample(range(100), 9)
    get_logger.info(
        f"Generated random 9-numbers_operations list {unsorted_numbers_list} "
    )
    yield unsorted_numbers_list
