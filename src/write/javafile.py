"""Write to Java file"""

import os
import re

from globals import *
import modfile


def write():
    """Write to Java file"""

    PACKAGE = modfile.get('package')
    FOLDER = OUTPUT_FOLDER + 'src/main/java/' + PACKAGE.replace('.', '/') + '/'
    os.makedirs(FOLDER)

    # Prepare blocks and items

    validMaterials = [
        "AIR", "ANVIL", "BARRIER", "CACTUS", "CAKE", "CARPET", "CIRCUITS", "CLAY", "CLOTH", "CORAL",
        "CRAFTED_SNOW", "DRAGON_EGG", "FIRE", "GLASS", "GOURD", "GRASS", "GROUND", "ICE", "IRON", "LAVA",
        "LEAVES", "PACKED_ICE", "PISTON", "PLANTS", "PORTAL", "REDSTONE_LIGHT", "ROCK", "SAND", "SNOW",
        "SPONGE", "TNT", "VINE", "WATER", "WEB", "WOOD"
    ]
    existingTabs = [
        "BREWING", "BUILDING_BLOCKS", "COMBAT", "DECORATIONS", "FOOD", "HOTBAR", "INVENTORY", "MATERIALS",
        "MISC", "REDSTONE", "SEARCH", "TOOLS", "TRANSPORTATION"
    ]
    soundTypes = [
        "ANCIENT_DEBRIS", "ANVIL", "BAMBOO", "BAMBOO_SAPLING", "BASALT", "BONE", "CHAIN", "CLOTH", "CORAL",
        "CROP", "FUNGUS", "GILDED_BLACKSTONE", "GLASS", "GROUND", "HONEY", "HYPHAE", "LADDER", "LANTERN",
        "LILY_PADS", "LODESTONE", "METAL", "NETHER_BRICK", "NETHER_GOLD", "NETHER_ORE", "NETHER_SPROUT",
        "NETHER_VINE", "NETHER_VINE_LOWER_PITCH", "NETHER_WART", "NETHERITE", "NETHERRACK", "NYLIUM",
        "PLANT", "ROOT", "SAND", "SCAFFOLDING", "SHROOMLIGHT", "SLIME", "SNOW", "SOUL_SAND", "SOUL_SOIL",
        "STEM", "STONE", "SWEET_BERRY_BUSH", "VINE", "WART", "WET_GRASS", "WOOD"
    ]

    BLOCKS = modfile.get('blocks') or {}
    ITEMS = modfile.get('items') or {}
    blocksContent = '\n\t\t'
    itemsContent = '\n\t\t'

    # Add items
    for item, data in ITEMS.items():

        stackSize = data["stackSize"]
        tab = data["inventoryTab"]

        if not tab.upper() in existingTabs:
            tab = 'misc'
        tab = 'ItemGroup.' + tab.upper()

        itemsContent += f'addItem("{item}", {stackSize}, {tab});\n\t\t'

    # Add blocks and block-items
    for block, data in BLOCKS.items():

        material = data["material"]
        hardness = data["hardness"]
        sound = data["sound"]
        light = data["light"]

        if not sound.upper() in soundTypes:
            sound = 'metal'
        sound = 'SoundType.' + sound.upper()

        if not material.upper() in validMaterials:
            material = 'ROCK'
        material = 'Material.' + material.upper()

        commonArgs = f'"{block}", {material}, {hardness}f, {sound}, {light}'

        if data["itemForm"]:
            stackSize = data["stackSize"]
            tab = data["inventoryTab"]
            if not tab.upper() in existingTabs:
                tab = 'misc'
            tab = 'ItemGroup.' + tab.upper()
            blocksContent += f'addBlockItem({commonArgs}, {stackSize}, {tab});\n\t\t'
        else:
            blocksContent += f'addBlock({commonArgs});\n\t\t'

    # Read template
    fc = ''
    with open('src/files/template.java', 'r') as file:
        fc = file.read()

    # Replacements
    fc = fc.replace('$PACKAGE', modfile.get('package'))
    fc = fc.replace('$MODID', modfile.get('modid'))
    fc = fc.replace('$BLOCKS', blocksContent)
    fc = fc.replace('$ITEMS', itemsContent)
    fc = re.sub(r'^\s*\/\/#.+$', '', fc)

    # Write to Java file
    with open(FOLDER + 'Main.java', 'w') as file:
        file.write(fc)
