"""Write to Java file"""

import os
import re

from globals import *
import modfile

PACKAGE = ''
FOLDER = ''

customTabs = {}
customTabsContent = '\n\t'
tabIndex = 11


def write():
    """Write to Java files"""

    global PACKAGE, FOLDER
    PACKAGE = modfile.get('package')
    FOLDER = OUTPUT_FOLDER + 'src/main/java/' + PACKAGE.replace('.', '/') + '/'
    os.makedirs(FOLDER, exist_ok=True)

    write_file('Main.java', {})
    write_file('ModBlocks.java', prepare_blocks())
    write_file('ModItems.java', prepare_items())
    write_file('ModTabs.java', {"tabs": customTabsContent})


def write_file(filename, cfg):
    """Write to Java file"""

    # Read
    fc = ''
    with open(STATIC_PATH + 'java/' + filename, 'r') as file:
        fc = file.read()

    # Replacements
    fc = fc.replace('$PACKAGE', modfile.get('package'))
    fc = fc.replace('$MODID', modfile.get('modid'))
    fc = fc.replace('$BLOCKS', cfg["blocks"] if "blocks" in cfg else '')
    fc = fc.replace('$ITEMS', cfg["items"] if "items" in cfg else '')
    fc = fc.replace('$TABS', cfg["tabs"] if "tabs" in cfg else '')

    # Write
    with open(FOLDER + filename, 'w') as file:
        file.write(fc)


def prepare_blocks():
    """Configure mod blocks"""

    BLOCKS = modfile.get('blocks') or {}
    blocksContent = ''

    # Add blocks and block-items
    for block, data in BLOCKS.items():

        # Get values
        itemForm = getKey(data, "itemForm").lower()
        solid = getKey(data, "solid").lower()
        hardness = getKey(data, "hardness")
        resistance = getKey(data, "resistance")
        stackSize = itemForm and getKey(data, "stackSize") or 0
        sound = 'SoundType.' + preset("soundTypes", getKey(data, "sound"))
        material = 'Material.' + preset("materials", getKey(data, "material"))
        mapColor = 'MaterialColor.' + preset("mapColors", getKey(data, "mapDisplay"))
        tab = itemForm and create_tab(data, 'ModBlocks.' + block.upper())

        # Add constructor
        args = f'"{block}", {itemForm}, {solid}, {material}, {mapColor}, {hardness}f, {resistance}f, {sound}, {stackSize}, {tab}'
        blocksContent += f'\n\tpublic static final Block {block.upper()} = addBlock({args});'

    return {"blocks": blocksContent}


def prepare_items():
    """Configure mod items"""

    ITEMS = modfile.get('items') or {}
    itemsContent = ''

    # Add items
    for item, data in ITEMS.items():

        # Get values
        stackSize = getKey(data, "stackSize")
        tab = create_tab(data, 'ModItems.' + item.upper())

        # Add constructor
        args = f'"{item}", {stackSize}, {tab}'
        itemsContent += f'\n\tpublic static final Item {item.upper()} = addItem({args});'

    return {"items": itemsContent}


def create_tab(data, icon):
    """Create custom inventory tab"""

    name = getKey(data, "inventoryTab")
    if not name:
        return 'null'

    tab_id = re.sub(r'[^\w\d]', '_', name).upper()
    tab_var = 'null'

    if preset("existingTabs", tab_id, True):
        tab_var = 'ItemGroup.' + tab_id
        return tab_var
    else:
        tab_var = 'ModTabs.' + tab_id
        if tab_id in customTabs:
            return tab_var

    customTabs[tab_id] = name

    global tabIndex
    tabIndex += 1

    content = f"""
    public static final ItemGroup {tab_id.upper()} = new ItemGroup({tabIndex}, "{tab_id.lower()}") {{
        public ItemStack createIcon() {{
            return new ItemStack({icon});
        }}
    }};
    """

    global customTabsContent
    customTabsContent += content

    return tab_var


def preset(mode, val, bool=False):
    """Variables"""

    values = {
        "materials": [
            "AIR", "ANVIL", "BARRIER", "CACTUS", "CAKE", "CARPET", "CIRCUITS", "CLAY", "CLOTH",
            "CORAL", "CRAFTED_SNOW", "DRAGON_EGG", "FIRE", "GLASS", "GOURD", "GRASS", "GROUND",
            "ICE", "IRON", "LAVA", "LEAVES", "PACKED_ICE", "PISTON", "PLANTS", "PORTAL",
            "REDSTONE_LIGHT", "ROCK", "SAND", "SNOW", "SPONGE", "TNT", "VINE", "WATER", "WEB", "WOOD"
        ],
        "mapColors": [
            "ADOBE", "AIR", "BLACK", "BLACK_TERRACOTTA", "BLUE", "BLUE_TERRACOTTA", "BROWN",
            "BROWN_TERRACOTTA", "CLAY", "CRIMSON_HYPHAE", "CRIMSON_NYLIUM", "CRIMSON_STEM", "CYAN",
            "CYAN_TERRACOTTA", "DIAMOND", "DIRT", "EMERALD", "FOLIAGE", "GOLD", "GRASS", "GRAY",
            "GRAY_TERRACOTTA", "GREEN", "GREEN_TERRACOTTA", "ICE", "IRON", "LAPIS", "LIGHT_BLUE",
            "LIGHT_BLUE_TERRACOTTA", "LIGHT_GRAY", "LIGHT_GRAY_TERRACOTTA", "LIME",
            "LIME_TERRACOTTA", "MAGENTA", "MAGENTA_TERRACOTTA", "NETHERRACK", "OBSIDIAN",
            "ORANGE_TERRACOTTA", "PINK", "PINK_TERRACOTTA", "PURPLE", "PURPLE_TERRACOTTA", "QUARTZ",
            "RED", "RED_TERRACOTTA", "SAND", "SNOW", "STONE", "TNT", "WARPED_HYPHAE",
            "WARPED_NYLIUM", "WARPED_STEM", "WARPED_WART", "WATER", "WHITE_TERRACOTTA", "WOOD",
            "WOOL", "YELLOW", "YELLOW_TERRACOTTA"
        ],
        "existingTabs": [
            "BREWING", "BUILDING_BLOCKS", "COMBAT", "DECORATIONS", "FOOD", "HOTBAR", "INVENTORY",
            "MATERIALS", "MISC", "REDSTONE", "SEARCH", "TOOLS", "TRANSPORTATION"
        ],
        "soundTypes": [
            "ANCIENT_DEBRIS", "ANVIL", "BAMBOO", "BAMBOO_SAPLING", "BASALT", "BONE", "CHAIN",
            "CLOTH", "CORAL", "CROP", "FUNGUS", "GILDED_BLACKSTONE", "GLASS", "GROUND", "HONEY",
            "HYPHAE", "LADDER", "LANTERN", "LILY_PADS", "LODESTONE", "METAL", "NETHER_BRICK",
            "NETHER_GOLD", "NETHER_ORE", "NETHER_SPROUT", "NETHER_VINE", "NETHER_VINE_LOWER_PITCH",
            "NETHER_WART", "NETHERITE", "NETHERRACK", "NYLIUM", "PLANT", "ROOT", "SAND",
            "SCAFFOLDING", "SHROOMLIGHT", "SLIME", "SNOW", "SOUL_SAND", "SOUL_SOIL", "STEM", "STONE",
            "SWEET_BERRY_BUSH", "VINE", "WART", "WET_GRASS", "WOOD"
        ]
    }
    defaults = {
        "materials": "ROCK",
        "mapColors": "STONE",
        "soundTypes": "METAL"
    }

    val = val.upper()
    isValid = val in values[mode]
    if (bool): return isValid
    return isValid and val or defaults[mode]


def getKey(data, key):
    """Key retrieval with edge guards"""
    return key in data and str(data[key]) or ''
