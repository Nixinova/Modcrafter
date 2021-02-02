"""Modfile configuration"""

import os
import re
import time
import yaml

global modfile_content
modfile_content = {}


def default():
    """Default Modfile contents"""

    with open('src/static/Modcrafter.yml', 'r') as file:
        return yaml.safe_load(file)


def read():
    """Read Modfile contents"""

    global modfile_content
    modfile_content = default()

    modfilename = 'Modcrafter.yml'
    modfilename_temp = modfilename + '.temp'

    if os.path.exists(modfilename):
        with open(modfilename, 'r') as file:
            file_content = yaml.safe_load(file)
            if file_content:
                modfile_content = file_content
    else:
        with open(modfilename_temp, 'w') as file:
            yaml.dump({"versions": modfile_content["1_versions"]}, file)
            file.write('\n')
            yaml.dump({"mod": modfile_content["2_mod"]}, file)
            file.write('\n')
            yaml.dump({"blocks": modfile_content["blocks"]}, file)
            file.write('\n')
            yaml.dump({"items": modfile_content["items"]}, file)
        with open(modfilename_temp, 'r') as file:
            with open(modfilename, 'w') as write:
                for ln in file:
                    write.write(re.sub(r'\d_', '', ln))
        os.remove(modfilename_temp)

    return modfile_content


def get(item):
    """Retrieves a config entry with edge guards"""

    result = ''

    if item == 'modid':
        return get('id') or get('name').lower().replace(' ', '')

    if item == 'package':
        authorID = re.sub(r"[^\w\d]", '', get('author')).lower()
        return f"src.{authorID}.{get('modid')}"

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
