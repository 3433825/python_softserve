import logging as log
from datetime import datetime


def basic_logger():
    filename = '{:%Y-%m-%d}.log'.format(datetime.now())
    log.basicConfig(filename=filename,
                    level=log.INFO,
                    format='[%(asctime)s] %(levelname)s %(filename)s %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')


basic_logger()
log.info('"Example of basic logging"')
