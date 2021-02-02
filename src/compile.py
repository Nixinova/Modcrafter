"""Compilation"""

import os

from globals import *
import modfile


def run():
    """Compile mod to jar"""

    filename = modfile.get('modid') + '-' + modfile.get('version') + '.jar'
    compiled_file = OUTPUT_FOLDER + 'build/libs/' + filename

    print(f"Compiling {filename}...")
    os.system(f'cd {OUTPUT_FOLDER} && gradlew build')

    try:
        if not os.path.exists(JAR_FOLDER):
            os.mkdir(JAR_FOLDER)
        os.rename(compiled_file, JAR_FOLDER + filename)
        print("Successfully compiled " + filename)
        print("Find file in ./" + JAR_FOLDER + filename)
    except FileExistsError:
        print(f"Version {modfile.get('version')} already exists. Please change the version number and try again, or set the `wip` key to `true` to generate automatic version IDs.")
    except:
        print("Compilation failed.")

# make compile
if __name__ == '__main__':
    modfile.read()
    run()
