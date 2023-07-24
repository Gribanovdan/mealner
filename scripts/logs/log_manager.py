import logging
import os

#
# log_file = os.path.join(os.path.dirname(__file__), 'log.log')
# logging.basicConfig(level=logging.INFO, filename=log_file, filemode="w",
#                     format="%(asctime)s %(levelname)s: %(message)s", force=True)
#

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def setup_logger(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


log_file = os.path.join(os.path.dirname(__file__), 'log.log')
debug_file = os.path.join(os.path.dirname(__file__), 'debug.log')
logger_debug = setup_logger('logger_debug', debug_file, logging.DEBUG)
logger_main = setup_logger('logger_main', log_file, logging.INFO)


def log(text: str, level: int):
    if level <= 10:
        logger_debug.debug(text)
    else:
        logger_main.log(level=level, msg=text)
