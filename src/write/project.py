"""Write meta project files"""

import os

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

    logger.log('Initialising project.')

    os.makedirs(TEXTURES_FOLDER, exist_ok=True)

    with open(modfile.modfilename, 'w') as file:
        file.write(modfile.default(True))

    with open('READ_ME.log', 'w') as file:
        file.write(message + 'You may delete this file.')

    gitignore_content = ''
    if not os.path.exists('.gitignore'):
        open('.gitignore', 'w').close()
    with open(STATIC_PATH + 'gitignore.txt', 'r') as file:
        gitignore_content = file.read()
    with open('.gitignore', 'r+') as file:
        file.read()
        file.write(gitignore_content)

    #logger.close()
    raise SystemExit(message)
