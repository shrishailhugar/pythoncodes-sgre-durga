import logging

# logging.basicConfig(filename='logfile.log',level=logging.DEBUG)
logging.basicConfig(filename='logfile.log', level=10, filemode='w',
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s:%(process)d:%(module)s:%(lineno)d',
                    datefmt='%d/%m/%Y %A %B %H:%M:%S:%p')
                    #datefmt='%d/%m/%Y %I:%M:%S:%p')
logging.info('Hi Info')
logging.warning('Hi Warning')
logging.debug('Hi debug')
logging.critical('Hi Critical')
logging.error('Hi Error')
