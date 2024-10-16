import logging
from custom_logger import get_custom_logger


def log_test1():
    logger = get_custom_logger(logging.INFO)
    print(logger)
    logger.debug('Hi debugfrom test1')
    logger.info('Hi INFOfrom test1')
    logger.critical('Hi Criticalfrom test1')
    logger.error('Hi Errorfrom test1')
    logger.warning('Hi Warningfrom test1')


def log_test2():
    logger = get_custom_logger(logging.ERROR)
    print(logger)
    logger.debug('Hi debugfrom test2')
    logger.info('Hi INFOfrom test2')
    logger.critical('Hi Criticalfrom test2')
    logger.error('Hi Errorfrom test2')
    logger.warning('Hi Warningfrom test2')


log_test1()
log_test2()
