"""Compilation"""

import os

import modfile

OUTPUT_FOLDER = 'gen/lib/'
JAR_FOLDER = 'gen/jars/'


def run():
    """Compile mod to jar"""

    filename = modfile.get('modid') + '-' + modfile.get('version') + '.jar'
    compiled_file = OUTPUT_FOLDER + 'build/libs/' + filename

    print(f"Compiling {filename}...")
    os.system(f'cd {OUTPUT_FOLDER} && gradlew build')

    if os.path.exists(compiled_file):
        print(f"Successfully compiled {filename}")
        if not os.path.exists(JAR_FOLDER):
            os.mkdir(JAR_FOLDER)
        os.rename(compiled_file, JAR_FOLDER + filename)
        print("Find file in " + JAR_FOLDER + filename)
    else:
        print("Compilation failed.")
