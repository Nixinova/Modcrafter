"""Modify assets"""

import os
import json
import shutil

from globals import *
import modfile
from write.java import customTabs

MODID = ''
ASSETS_FOLDER = ''
BLOCKS = {}
ITEMS = {}


def write():
    """Create assets"""

    global MODID, ASSETS_FOLDER, BLOCKS, ITEMS
    MODID = modfile.get('modid')
    ASSETS_FOLDER = OUTPUT_FOLDER + 'src/main/resources/assets/' + MODID + '/'
    BLOCKS = modfile.get('blocks')
    ITEMS = modfile.get('items')

    os.makedirs(ASSETS_FOLDER, exist_ok=True)

    lang()
    blockstates()
    models()
    textures()


def lang():
    """Create lang file"""

    LANG_FOLDER = ASSETS_FOLDER + 'lang/'
    os.makedirs(LANG_FOLDER, exist_ok=True)

    langfile = LANG_FOLDER + 'en_us.json'

    content = {}

    for name, data in ITEMS.items():
        content[f'item.{MODID}.{name}'] = getKey(data, 'name') or name

    for name, data in BLOCKS.items():
        content[f'block.{MODID}.{name}'] = getKey(data, 'name') or name

    for tab_id, name in customTabs.items():
        content[f'itemGroup.{tab_id.lower()}'] = name

    with open(langfile, 'w') as file:
        file.write(json.dumps(content, indent=4))


def blockstates():
    """Create blockstates"""

    BLOCKSTATES_FOLDER = ASSETS_FOLDER + 'blockstates/'
    os.makedirs(BLOCKSTATES_FOLDER, exist_ok=True)

    for name, _ in BLOCKS.items():
        #content = {"forge_marker": 1, "variants": {"normal": [{"textures": {"all": f"{MODID}:block/{name}"}, "model": "cube_all", "uvlock": True}]}}
        content = {"variants": {"": {"model": f"{MODID}:block/{name}"}}}
        with open(BLOCKSTATES_FOLDER + name + '.json', 'w') as file:
            file.write(json.dumps(content, indent=4))


def models():
    """Create models"""

    MODELS_FOLDER = ASSETS_FOLDER + 'models/'
    os.makedirs(MODELS_FOLDER + 'block/', exist_ok=True)
    os.makedirs(MODELS_FOLDER + 'item/', exist_ok=True)

    for name, data in ITEMS.items():
        texture = getKey(data, 'textures') or 'auto'
        if texture == 'auto':
            texture = f'{MODID}:item/{name}'
        elif not ':' in texture:
            texture = MODID + ('/' in texture and ':' or ':item/') + texture
        content = {"parent": "minecraft:item/generated", "textures": {"layer0": texture}}

        with open(MODELS_FOLDER + 'item/' + name + '.json', 'w') as file:
            file.write(json.dumps(content, indent=4))

    for name, data in BLOCKS.items():
        content = {}
        textures = getKey(data, 'textures') or 'auto'
        default = f'{MODID}:block/{name}'

        if isinstance(textures, str):
            texture = textures == 'auto' and default or textures
            if not ':' in texture:
                texture = MODID + ('/' in texture and ':' or ':block/') + texture
            content = {"parent": "minecraft:block/cube_all", "textures": {"all": texture}}
        else:
            nameReplacement = f'{MODID}:block/{name}'

            def setTexture(side):
                if side in textures:
                    return textures[side].replace('$id', nameReplacement)
                return default

            content = {"parent": "block/cube", "textures": {
                "particle": setTexture('particle'),
                "up": setTexture('up'),
                "down": setTexture('down'),
                "north": setTexture('north'),
                "south": setTexture('south'),
                "east": setTexture('east'),
                "west": setTexture('west'),
            }}

        with open(MODELS_FOLDER + 'block/' + name + '.json', 'w') as file:
            file.write(json.dumps(content, indent=4))
        with open(MODELS_FOLDER + 'item/' + name + '.json', 'w') as file:
            file.write(json.dumps({"parent": f"{MODID}:block/{name}"}, indent=4))


def textures():
    """Copy over textures"""

    if os.path.exists(TEXTURES_FOLDER):
        shutil.copytree(TEXTURES_FOLDER, ASSETS_FOLDER + 'textures/', dirs_exist_ok=True)


def getKey(data, key):
    """Key retrieval with edge guards"""
    return key in data and data[key] or ''
