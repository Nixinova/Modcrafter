"""Modify assets"""

import os
import json
import shutil

from globals import *
import modfile

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
        content[f'item.{MODID}.{name}'] = f'{data["name"] or name}'

    for name, data in BLOCKS.items():
        content[f'block.{MODID}.{name}'] = f'{data["name"] or name}'

    with open(langfile, 'w') as file:
        file.write(json.dumps(content, indent=2))


def blockstates():
    """Create blockstates"""

    BLOCKSTATES_FOLDER = ASSETS_FOLDER + 'blockstates/'
    os.makedirs(BLOCKSTATES_FOLDER, exist_ok=True)

    for name, _ in BLOCKS.items():
        content = {"variants": {"normal": {"model": f"{MODID}:{name}"}}}
        with open(BLOCKSTATES_FOLDER + name + '.json', 'w') as file:
            file.write(json.dumps(content, indent=2))


def models():
    """Create models"""

    MODELS_FOLDER = ASSETS_FOLDER + 'models/'
    os.makedirs(MODELS_FOLDER, exist_ok=True)
    os.makedirs(MODELS_FOLDER + 'block/', exist_ok=True)
    os.makedirs(MODELS_FOLDER + 'item/', exist_ok=True)

    for name, _ in ITEMS.items():
        content = {"parent": "item/generated", "textures": {"layer0": f"{MODID}:{name}"}}
        with open(MODELS_FOLDER + 'item/' + name + '.json', 'w') as file:
            file.write(json.dumps(content, indent=2))

    for name, data in BLOCKS.items():
        content = {}
        textures = data["textures"]
        default = f'{MODID}:{name}'

        if isinstance(textures, str):
            texture = default if textures == 'auto' else f'{textures}'
            content = {"parent": "block/cube_all", "textures": {"all": texture}}
        else:
            nameReplacement = MODID + ':' + name

            def setTexture(side):
                if side in textures:
                    return textures[side].replace('$name', nameReplacement)
                return default

            content = {"parent": "block/cube", "textures": {
                "particle": setTexture('particle'),
                "top": setTexture('top'),
                "bottom": setTexture('bottom'),
                "north": setTexture('north'),
                "south": setTexture('south'),
                "east": setTexture('east'),
                "west": setTexture('west'),
            }}

        with open(MODELS_FOLDER + 'block/' + name + '.json', 'w') as file:
            file.write(json.dumps(content, indent=2))


def textures():
    """Copy over textures"""

    shutil.copytree(TEXTURES_FOLDER, ASSETS_FOLDER + 'textures/', dirs_exist_ok=True)