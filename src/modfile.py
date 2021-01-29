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
        "versions": {
            "_1_minecraft": "1.16.1",
            "_2_forge": "32.0.108"
        },
        "mod": {
            "_1_name": "My Mod",
            "_2_id": "mymod",
            "author": "Myself",
            "version": "v1.0",
            "wip": False,
            "description": "A simple mod.",
            # "license": "All rights reserved",
            # "bugs": "https://github.com/myself/mymod/issues",
            # "website": "https://example.com",
        },
        "blocks": {
            "example_block": {
                "_1_name": "Example Block",
                "_2_itemForm": True,
                "_3_textures": "auto",
                "material": "wood",
                "hardness": 2.5,
                "sound": "wood",
                "light": 1,
                "stackSize": 16,
                "inventoryTab": "misc"
            },
            "world_only_block": {
                "_1_name": "Block Without Item Form",
                "_2_itemForm": False,
                "_3_textures": {
                    "top": "$name_top",
                    "bottom": "$name_bottom"
                },
                "material": "rock",
                "sound": "metal",
                "light": 6,
                "hardness": 4.8
            }
        },
        "items": {
            "example_item": {
                "_1_name": "Example Item",
                "_3_textures": "auto",
                "stackSize": 16,
                "inventoryTab": "misc"
            }
        }
    }

    return content


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
            yaml.dump({"versions": modfile_content["versions"]}, file)
            file.write('\n')
            yaml.dump({"mod": modfile_content["mod"]}, file)
            file.write('\n')
            yaml.dump({"blocks": modfile_content["blocks"]}, file)
            file.write('\n')
            yaml.dump({"items": modfile_content["items"]}, file)
        with open(modfilename_temp, 'r') as file:
            with open(modfilename, 'w') as write:
                for ln in file:
                    write.write(re.sub(r'_\d_', '', ln))
        os.remove(modfilename_temp)

    return modfile_content


def get(item):
    """Retrieves a config entry with edge guards"""

    if item == 'modid':
        return get('id') or get('name').lower().replace(' ', '')

    if item == 'package':
        authorID = re.sub(r"[^\w\d]", '', get('author'))
        return f"com.{authorID.lower()}.{get('modid').lower()}"

    if item == 'version' and get('wip'):
        return 'dev-' + str(int(time.time()))[-5:]

    for key in modfile_content:
        if key == item:
            return modfile_content[key]
        for subkey in modfile_content[key]:
            if subkey == item:
                return modfile_content[key][item]
    return ''
