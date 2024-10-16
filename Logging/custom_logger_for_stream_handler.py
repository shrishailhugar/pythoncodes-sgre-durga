import logging

logger = logging.getLogger('demologger')
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(lineno)d:%(message)s',
                              datefmt='%d/%m/%Y %I:%M:%S:%p')
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.debug('Hi debug')
logger.info('Hi INFO')
logger.critical('Hi Critical')
logger.error('Hi Error')
logger.warning('Hi Warning')
