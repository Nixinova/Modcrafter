# Modcrafter Changelog

## 0.4
*2021-02-20*
- Added GUI for creating and compiling mods.

## 0.3
*2021-02-07*
- Added `mapDisplay` field for blocks to set the map color type.
- Added `solid` field for blocks to control whether the block stops entity movement.
- Added error logger, while places log files in folder `logs/`.
- Changed parsing to allow blocks to be empty of fields.
- Changed old `solid` field to `translucent` for blocks and inverted the value.
- Fixed custom inventory tabs not allowing display names.
- Fixed top and bottom faces of blocks being improperly set.

## 0.2
*2021-02-06*
- Added support for custom inventory tabs.
- Changed output to split Java files into separate block, item, and inventory tab classes.
- Fixed gitignore file being overwritten on initialisation.

## 0.1
*2021-02-04*
- Added support for blocks, with customisable texture mappings.
- Added support for items.
