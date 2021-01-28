"""Modfile configuration"""

import os
import re
import time
import yaml

global modfile_content
modfile_content = {}


def default():
    """Default Modfile contents"""

    content = {
        "mcver": "1.16.1",
        "forgever": "32.0.108",
        "modinfo": {
            "name": "My Mod",
            "id": "mymod",
            "author": "Myself",
            "version": "1.0",
            "description": "A simple mod.",
            # "license": "All rights reserved",
            # "bugs": "https://github.com/myself/mymod/issues",
            # "website": "https://example.com",
        }
    }

    return content


def read():
    """Read Modfile contents"""

    global modfile_content
    modfile_content = default()

    modfilename = 'Modcrafter.yml'

    if os.path.exists(modfilename):
        with open(modfilename, 'r') as file:
            file_content = yaml.safe_load(file)
            if file_content:
                modfile_content = file_content
    else:
        with open(modfilename, 'w') as file:
            yaml.dump(modfile_content, file)

    return modfile_content


def get(item):
    """Retrieves a Modfile item with edge guards"""

    if item == 'modid':
        return get('id') or get('name').lower().replace(' ', '')

    if item == 'package':
        authorID = re.sub(r"[^\w\d]", '', get('author'))
        return f"com.{authorID.lower()}.{get('modid').lower()}"
    
    if item == 'version':
        if get('dev'):
            return 'dev-' + str(int(time.time()))[-5:]

    for i in modfile_content:
        if i == item:
            return modfile_content[i]
        for key in modfile_content[i]:
            if key == item:
                return modfile_content[i][key]
    return ''
