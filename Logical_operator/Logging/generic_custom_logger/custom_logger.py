import logging
import inspect

def get_custom_logger(level):
    print(level)
    function_name=inspect.stack()[1][3]
    logger_name=function_name+' logger'
    logger=logging.getLogger(logger_name)
    fileHandler=logging.FileHandler(f"{function_name}.log",mode='a')
    # fileHandler.setLevel(level)
    formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(lineno)s:%(message)s',
                                datefmt='%d/%m/%Y %I:%M:%S:%p')
    fileHandler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(fileHandler)
    print(logger)
    return logger