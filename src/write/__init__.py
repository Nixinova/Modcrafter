"""Initializes project"""

import write.build_gradle as build_gradle
import write.mods_toml as mods_toml
import write.pack_mcmeta as pack_mcmeta
import write.javafile as javafile
import write.assets as assets

OUTPUT_FOLDER = 'gen/lib/'


def configure():
    """Run the initialization"""

    build_gradle.configure()
    mods_toml.configure()
    pack_mcmeta.configure()

    javafile.write()
    assets.write()
