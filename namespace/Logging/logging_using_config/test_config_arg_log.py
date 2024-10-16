import logging
import logging.config
logging.config.fileConfig('logging_config.init')
logger=logging.getLogger('demoLogger')
logger.debug('Hi debug')
logger.info('Hi INFO')
logger.critical('Hi Critical')
logger.error('Hi Error')
logger.warning('Hi Warning')
