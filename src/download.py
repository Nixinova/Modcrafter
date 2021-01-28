"""Downloads the Forge MDK"""

import os
import zipfile
import shutil
import requests

import modfile

OUTPUT_FOLDER = 'gen/lib/'


def download():
    """Downloads and extracts MDK"""

    prefix = 'https://files.minecraftforge.net/maven/net/minecraftforge/forge/'
    version = modfile.get('mcver') + '-' + modfile.get('forgever')
    url = prefix + version + '/forge-' + version + '-mdk.zip'
    zip_output = 'output.zip'

    # Download MDK
    req = requests.get(url, allow_redirects=True)
    with open(zip_output, 'wb') as file:
        file.write(req.content)

    # Extract MDK
    with zipfile.ZipFile(zip_output, 'r') as file:
        file.extractall(OUTPUT_FOLDER)
    os.remove(zip_output)

    cleanup()


def cleanup():
    """Cleans up output folder"""

    # Configure gitfiles
    os.remove(OUTPUT_FOLDER + '.gitattributes')
    with open(OUTPUT_FOLDER + '.gitignore', 'w') as file:
        file.write('.gradle\nbuild\ngradle\nmdk_info\n')

    # Move Forge metainfo into folder
    mdk_info = ['changelog.txt', 'CREDITS.txt', 'README.txt', 'LICENSE.txt']
    if os.path.exists(OUTPUT_FOLDER + 'mdk_info'):
        shutil.rmtree(OUTPUT_FOLDER + 'mdk_info')
    os.mkdir(OUTPUT_FOLDER + 'mdk_info')
    for file in mdk_info:
        os.rename(OUTPUT_FOLDER + file, OUTPUT_FOLDER + 'mdk_info/' + file)
    os.rename(OUTPUT_FOLDER + 'src/main/java/com/example/examplemod/ExampleMod.java',
              OUTPUT_FOLDER + 'mdk_info/ExampleMod.java')
    shutil.rmtree(OUTPUT_FOLDER + 'src/main/java/com')
