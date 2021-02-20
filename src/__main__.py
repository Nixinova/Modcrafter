"""Modcrafter"""

import gui.gui as gui
import runner
from globals import *


def ui():
    """Open Modcrafter GUI"""
    gui.run()


def run():
    """Run Modcrafter"""
    runner.run()


ui()
# try:
#    run()
# except Exception as err:
#    logger.error(err)
