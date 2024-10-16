import logging

logger = logging.getLogger('demologger')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('test2.log',mode='w')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(lineno)d:%(message)s',
                              datefmt='%d/%m/%Y %I:%M:%S:%p')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.debug('Hi debug from test2')
logger.info('Hi INFO from test2')
logger.critical('Hi Critical from test2')
logger.error('Hi Error from test2')
logger.warning('Hi Warning from test2')
