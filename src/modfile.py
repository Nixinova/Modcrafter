"""Modfile configuration"""

import os
import yaml

global modfile_content
modfile_content = {}


def default():
    """Default Modfile contents"""

    content = {
        "meta": {
            "name": "My Mod",
            "id": "mymod",
            "author": "Myself",
            "version": "1.0",
            "description": "A simple mod.",
            #"license": "All rights reserved",
            #"bugs": "https://github.com/myself/mymod/issues",
            #"website": "https://example.com",
        }
    }

    return content


def read():
    """Read Modfile contents"""

    global modfile_content
    modfile_content = default()

    if os.path.exists('Modfile'):
        with open('Modfile', 'r') as file:
            file_content = yaml.safe_load(file)
            if file_content:
                modfile_content = file_content
    else:
        with open('Modfile', 'w') as file:
            yaml.dump(modfile_content, file)

    return modfile_content


def get(item):
    """Retrieves a Modfile item with edge guards"""

    for i in modfile_content:
        if i == item:
            return modfile_content[i]
        for key in modfile_content[i]:
            if key == item:
                return modfile_content[i][key]
    return ''
