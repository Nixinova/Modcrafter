"""Downloads the Forge MDK"""

import os
import zipfile
import shutil

import requests

from globals import *
import modfile


def download():
    """Downloads and extracts MDK"""

    prefix = 'https://files.minecraftforge.net/maven/net/minecraftforge/forge/'
    version = modfile.get('minecraft') + '-' + modfile.get('forge')
    url = prefix + version + '/forge-' + version + '-mdk.zip'
    zip_output = 'output.zip'

    # Download MDK
    req = requests.get(url, allow_redirects=True)
    if b"404 Not Found" in req.content:
        error = f'Failed to download MDK version "{version}". This is most likely due to invalid configuration. Please try again.'
        raise FileNotFoundError(error)
    with open(zip_output, 'wb') as file:
        file.write(req.content)

    # Extract MDK
    shutil.rmtree(OUTPUT_FOLDER, ignore_errors=True)
    with zipfile.ZipFile(zip_output, 'r') as file:
        file.extractall(OUTPUT_FOLDER)
    os.remove(zip_output)

    try:
        cleanup()
    except:
        print("Folder cleanup failed.")


def cleanup():
    """Cleans up output folder"""

    # Configure gitfiles
    # with open(OUTPUT_FOLDER + '.gitattributes', 'w') as file:
    #    file.write('src/generated/**/*.json text eol=lf')
    os.remove(OUTPUT_FOLDER + '.gitattributes')
    with open(OUTPUT_FOLDER + '.gitignore', 'w') as file:
        file.write('.gradle/\nbuild/\nlogs/\nmdk_info/\n')

    # Move Forge metainfo into folder
    mdk_info = ['changelog.txt', 'CREDITS.txt', 'README.txt', 'LICENSE.txt']
    shutil.rmtree(OUTPUT_FOLDER + 'mdk_info', ignore_errors=True)
    os.mkdir(OUTPUT_FOLDER + 'mdk_info')
    for file in mdk_info:
        os.rename(OUTPUT_FOLDER + file, OUTPUT_FOLDER + 'mdk_info/' + file)
    os.rename(OUTPUT_FOLDER + 'src/main/java/com/example/examplemod/ExampleMod.java',
              OUTPUT_FOLDER + 'mdk_info/ExampleMod.java')
    shutil.rmtree(OUTPUT_FOLDER + 'src/main/java/com')


# make setup
if __name__ == '__main__':
    modfile.read()
    download()
