"""Modcrafter control panel"""

import modfile
import download as mdk
import write as files
import compile as compiler
import logger
from globals import *


def run():
    """Run Modcrafter"""
    logger.start()
    modfile.read()
    mdk.download()
    files.configure()
    compiler.run()
    logger.close()
