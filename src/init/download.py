import os
import re
import zipfile
import shutil
import requests

OUTPUT_FOLDER = 'gen/lib/'

def download():
    """Downloads and extracts MDK"""

    prefix = 'https://files.minecraftforge.net/maven/net/minecraftforge/forge/'
    version = '1.16.1-32.0.108'
    url = prefix + version + '/forge-' + version + '-mdk.zip'
    zip_output = 'output.zip'

    # Download MDK
    req = requests.get(url, allow_redirects=True)
    with open(zip_output, 'wb') as zip:
        zip.write(req.content)

    # Extract MDK
    with zipfile.ZipFile(zip_output, 'r') as zip_ref:
        zip_ref.extractall(OUTPUT_FOLDER)
    os.remove(zip_output)
    
    cleanup()


def cleanup():
    """Cleans up output folder"""

    shutil.rmtree(OUTPUT_FOLDER + 'src/main/java/com')
    os.remove(OUTPUT_FOLDER + '.gitattributes')
    open(OUTPUT_FOLDER + '.gitignore', 'w').write('.gradle\nbuild\ngradle\nmdk_info\n')
    
    mdk_info = ['changelog.txt', 'CREDITS.txt', 'README.txt', 'LICENSE.txt']
    shutil.rmtree(OUTPUT_FOLDER + 'mdk_info')
    os.mkdir(OUTPUT_FOLDER + 'mdk_info')
    for file in mdk_info:
        os.rename(OUTPUT_FOLDER + file, OUTPUT_FOLDER + 'mdk_info/' + file)
