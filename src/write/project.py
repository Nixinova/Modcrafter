"""Write meta project files"""

import os
import re

from globals import *
import logger
import modfile

message = (
    'Successfully initialised Modcrafter project.\n'
    'Configure Modcrafter.yml then run this EXE file again to compile to a JAR.\n'
    f'Make sure to put any custom textures into {TEXTURES_FOLDER} before running the EXE.\n'
)


def init():
    """Initialise project"""
    logger.log('Initialising project')

    os.makedirs(TEXTURES_FOLDER, exist_ok=True)

    with open(modfile.modfilename, 'w') as file:
        file.write(modfile.default(True))

    with open('README.log', 'w') as file:
        file.write(message + '\nYou may delete this file.')

    if not os.path.exists('.gitignore'):
        open('.gitignore', 'w').close()
    with open('.gitignore', 'r+') as file:
        file.read()
        file.write(re.sub(r'(?m)^ {12}', '', """
            # Mod build files
            .gradle/
            build/
            mdk_info/

            # Outputted jar files
            *.jar

            # Logs
            *.log
        """.rstrip()))

    logger.close()
    raise SystemExit(message)
