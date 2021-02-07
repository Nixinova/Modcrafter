"""Compilation"""

import os

from logger import log
from globals import *
import modfile


def run():
    """Compile mod to jar"""

    filename = modfile.get('modid') + '-' + modfile.get('version') + '.jar'
    compiled_file = OUTPUT_FOLDER + 'build/libs/' + filename

    log(f"Compiling {filename}...")
    os.system(f'cd {OUTPUT_FOLDER} && gradlew build --warn')

    try:
        filepath = JAR_FOLDER + filename
        os.makedirs(JAR_FOLDER, exist_ok=True)
        if os.path.exists(filepath):
            os.remove(filepath)
        os.rename(compiled_file, filepath)
        log("Successfully compiled " + filename)
        log("Find file in ./" + filepath)
    except:
        log("Compilation failed.")

# make compile
if __name__ == '__main__':
    modfile.read()
    run()
