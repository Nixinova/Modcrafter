"""Global variables"""

import os

VERSION = '0.2_next'

MAIN_FOLDER = 'lib/'
OUTPUT_FOLDER = MAIN_FOLDER + 'mod/'
JAR_FOLDER = MAIN_FOLDER + 'jars/'
TEXTURES_FOLDER = MAIN_FOLDER + 'textures/'

MODULE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/'
STATIC_PATH = MODULE_PATH + 'static/'

LOGS_FOLDER = 'logs/'
