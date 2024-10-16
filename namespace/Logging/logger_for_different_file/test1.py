import logging
import test2
logger = logging.getLogger('demologger')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('test1.log',mode='w')
file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(lineno)d:%(message)s',
                              datefmt='%d/%m/%Y %I:%M:%S:%p')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.debug('Hi debug from test1')
logger.info('Hi INFO from test1')
logger.critical('Hi Critical from test1')
logger.error('Hi Error from test1')
logger.warning('Hi Warning from test1')

