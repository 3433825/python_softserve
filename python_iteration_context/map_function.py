"""
Add to every element 10

The map() function in Python is a built-in function that allows you to apply a specified function to all the
items in an input list (or any iterable) and returns an iterator of the results. It takes two arguments:
the function to be applied and the iterable.
The basic syntax of map() is:
map(function, iterable)
for instance:

"""
# import logging
# from datetime import datetime
from Data import data
from modules import advanced_logg

# simple way
# logging.basicConfig(filename='iteration_context_local_logs.log',
#                     level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %H:%M:%S')

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
#
# # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
# formatter = logging.Formatter(
#     fmt='[%(asctime)s] %(levelname)s %(filename)s %(message)s',
#     datefmt='%Y-%m-%d %H-%M-%S')
#
# # file_handler = logging.FileHandler('iteration_context_local_logs.log')
# file_handler = logging.FileHandler(
#     '{:%Y-%m-%d}.log'.format(datetime.now()),
#     mode='a'
# )
#
# file_handler.setLevel(logging.INFO)
# file_handler.setFormatter(formatter)
#
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)
#
# logger.addHandler(file_handler)
# # logger.addHandler(stream_handler)

logger = advanced_logg.advanced_logger()


def add_n(x, n):
    x += n
    # logs.warning("element increased on 10")
    return x


def add_n_to_sequence_lambda(sequence, n):
    added_n = list(map(lambda x: x + n, sequence))
    logger.info(f"adding {n} to every element of {sequence}")
    return added_n


def add_n_to_sequence_func(func, sequence, n):
    return list(map(func, sequence, n))


logger.info(f"initial list: {data.UNSORTED_NUMBERS_LIST}")
print()
result = add_n_to_sequence_lambda(data.UNSORTED_NUMBERS_LIST, 10)
# print(f"with lambda: {result}")
logger.info(f"with lambda: {result}")
# result = add_n_to_sequence_func(add_n, data.UNSORTED_NUMBERS_LIST, 10)
# logging.info(f"with function: {result}")
