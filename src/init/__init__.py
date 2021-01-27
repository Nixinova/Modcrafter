"""Initializes project"""

import os
import re
import zipfile
import shutil
import requests

import init.download as mdk
import init.build_gradle as configure

OUTPUT_FOLDER = 'gen/lib/'

def run():
    mdk.download()
    build_gradle.configure()
