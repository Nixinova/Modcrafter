"""Logging code"""

import os
import datetime as date
import logging
import re

from globals import *

logger = None
timestamp = re.sub(r'[-: ]|\..+$', '', str(date.datetime.now()))
logfile = LOGS_FOLDER + 'Modcrafter_' + timestamp + '.log'


def start():
    """Start logger"""

    os.makedirs(LOGS_FOLDER, exist_ok=True)

    logging.basicConfig(
        filename=logfile,
        level=logging.DEBUG,
        format='<%(asctime)s> %(levelname)s @ %(name)s: %(message)s',
        datefmt='%Y-%m-%d_%H:%M:%S'
    )
    global logger
    logger = logging.getLogger()

    print(f"--- Modcrafter {VERSION} ---")
    print('')
    logger.info(f"Running Modcrafter {VERSION}")


def close():
    """Close logger and delete if error-free"""
    logger.info("Modcrafter mod compilation complete.")
    for handler in logging.getLogger().handlers:
        handler.close()
        logger.removeHandler(handler)
    os.remove(logfile)


def log(msg):
    """Log message to both output file and console"""
    logger.info(msg)
    print(msg)


def error(err, suppress=False):
    """Log error to both output file and console"""
    print(f"Traceback logged to {logfile}")
    logger.exception(err)
    if not suppress:
        raise err
