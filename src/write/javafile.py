"""Write to Java file"""

import os

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

    def getKey(data, key):
        return key in data and str(data[key]) or ''

    # Add items
    for item, data in ITEMS.items():

        stackSize = getKey(data, "stackSize")
        tab = getKey(data, "inventoryTab").upper()

        tab = 'ItemGroup.' + (tab in existingTabs and tab or 'MISC')

        itemsContent += f'addItem("{item}", {stackSize}, {tab});\n\t\t'

    # Add blocks and block-items
    for block, data in BLOCKS.items():

        itemForm = getKey(data, "itemForm").lower()
        solid = getKey(data, "solid").lower()
        material = getKey(data, "material").upper()
        hardness = getKey(data, "hardness")
        resistance = getKey(data, "resistance")
        sound = getKey(data, "sound").upper()
        stackSize = itemForm and getKey(data, "stackSize") or 0
        tab = itemForm and getKey(data, "inventoryTab").upper() or 'null'

        sound = 'SoundType.' + (sound in soundTypes and sound or 'METAL')
        material = 'Material.' + (material in validMaterials and material or 'ROCK')
        tab = itemForm and 'ItemGroup.' + (tab in existingTabs and tab or 'MISC') or 'null'

        args = f'"{block}", {itemForm}, {solid}, {material}, {hardness}f, {resistance}f, {sound}, {stackSize}, {tab}'
        blocksContent += f'addBlock({args});\n\t\t'

    # Read template
    fc = ''
    with open('src/static/Main.java', 'r') as file:
        fc = file.read()

    # Replacements
    fc = fc.replace('$PACKAGE', modfile.get('package'))
    fc = fc.replace('$MODID', modfile.get('modid'))
    fc = fc.replace('$BLOCKS', blocksContent)
    fc = fc.replace('$ITEMS', itemsContent)

    # Write to Java file
    with open(FOLDER + 'Main.java', 'w') as file:
        file.write(fc)
