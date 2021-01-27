"""Initializes project"""

import init.download as mdk
import init.build_gradle as build_gradle
import init.mods_toml as mods_toml
import init.pack_mcmeta as pack_mcmeta
import modfile

OUTPUT_FOLDER = 'gen/lib/'


def run():
    """Run the initialization"""

    modfile.read()
    mdk.download()
    build_gradle.configure()
    mods_toml.configure()
    pack_mcmeta.configure()
