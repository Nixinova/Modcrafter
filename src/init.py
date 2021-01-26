"""Initializes project"""

import os
import re
import zipfile
import shutil
import requests

from src.files.modfile import default

OUTPUT_FOLDER = 'gen/lib/'


def init():
    """Initializes project"""
    download()
    cleanup()


def download():
    """Downloads and extracts MDK"""

    prefix = 'https://files.minecraftforge.net/maven/net/minecraftforge/forge/'
    version = '1.16.1-32.0.108'
    url = prefix + version + '/forge-' + version + '-mdk.zip'
    zip_output = 'output.zip'

    # Download MDK
    req = requests.get(url, allow_redirects=True)
    open(zip_output, 'wb').write(req.content)

    # Extract MDK
    with zipfile.ZipFile(zip_output, 'r') as zip_ref:
        zip_ref.extractall(OUTPUT_FOLDER)
    os.remove(zip_output)


def cleanup():
    """Cleans up output folder"""

    to_remove = [
        'changelog.txt', 'CREDITS.txt', 'README.txt', 'LICENSE.txt',
        '.gitignore', '.gitattributes'
    ]
    shutil.rmtree(OUTPUT_FOLDER + 'src/main/java/com')
    for file in to_remove:
        os.remove(OUTPUT_FOLDER + file)
    open(OUTPUT_FOLDER + '.gitignore', 'w').write('build\n.gradle\ngradle\n')


def settings():
    """Configure mod settings"""
    modfile_content = ''
    if os.path.exists('Modfile'):
        modfile_content = open('Modfile', 'r').read()
    else:
        modfile_content = default()
    buildcfg = open(OUTPUT_FOLDER + 'build.gradle', 'r').read()
    buildcfg = re.sub(r'\/\/.+$', r'', buildcfg)
