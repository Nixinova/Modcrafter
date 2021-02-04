"""Compilation"""

import os

from globals import *
import modfile


def run():
    """Compile mod to jar"""

    filename = modfile.get('modid') + '-' + modfile.get('version') + '.jar'
    compiled_file = OUTPUT_FOLDER + 'build/libs/' + filename

    print(f"Compiling {filename}...")
    os.system(f'cd {OUTPUT_FOLDER} && gradlew build --warn')

    try:
        filepath = JAR_FOLDER + filename
        os.makedirs(JAR_FOLDER, exist_ok=True)
        if os.path.exists(filepath):
            os.remove(filepath)
        os.rename(compiled_file, filepath)
        print("Successfully compiled " + filename)
        print("Find file in ./" + filepath)
    except:
        print("Compilation failed.")

# make compile
if __name__ == '__main__':
    modfile.read()
    run()
