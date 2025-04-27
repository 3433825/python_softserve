import logging
from datetime import datetime


def advanced_logger(path='./{:%Y-%m-%d}.log'):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt=f'[%(asctime)s] %(levelname)s %(filename)s %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S')

    # file_handler = logging.FileHandler(
    #     '../logs/{:%Y-%m-%d}.log'.format(datetime.now()),
    #     mode='a'
    # )

    file_handler = logging.FileHandler(
        path.format(datetime.now()),
        mode='a'
    )

    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # stream_handler = logging.StreamHandler()
    # stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    # logger.addHandler(stream_handler)

    return logger


# advanced_logger().info('Example of advanced logger')
