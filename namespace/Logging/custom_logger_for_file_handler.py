import logging

logger = logging.getLogger('demologger')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('savelog.log',mode='w')
file_handler.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(lineno)d:%(message)s',
                              datefmt='%d/%m/%Y %I:%M:%S:%p')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.debug('Hi debug')
logger.info('Hi INFO')
logger.critical('Hi Critical')
logger.error('Hi Error')
logger.warning('Hi Warning')
