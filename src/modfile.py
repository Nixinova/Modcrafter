"""Mod configuration file"""

import os
import re
import time
import yaml

from globals import *
import write.project as project

modfilename = 'Modcrafter.yml'
modfile_content = {}


def default(raw):
    """Default config contents"""

    with open(STATIC_PATH + modfilename, 'r') as file:
        yaml_content = ''.join(file.readlines())
        global modfile_content
        modfile_content = yaml.safe_load(yaml_content)
        return raw and yaml_content or yaml.safe_load(yaml_content)


def read():
    """Read config contents"""

    default(False)

    if os.path.exists(modfilename):
        with open(modfilename, 'r') as file:
            file_content = yaml.safe_load(file)
            if file_content:
                global modfile_content
                modfile_content = file_content
    else:
        project.init()


def get(item):
    """Retrieves a config entry with edge guards"""

    result = ''

    if item == 'modid':
        return get('id') or get('name').lower().replace(' ', '')

    if item == 'package':
        authorID = re.sub(r"[^\w\d]", '', get('author')).lower()
        return f"mod.{authorID}.{get('modid')}"

    for key in modfile_content:
        if key == item:
            result = modfile_content[key]
        for subkey in modfile_content[key]:
            if subkey == item:
                result = modfile_content[key][item]

    if item == 'version':
        if result == 'auto':
            return 'dev-' + str(int(time.time()))[-5:]
        return str(result)

    return result
