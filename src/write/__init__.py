"""Initializes project"""

import write.config as config
import write.javafile as javafile
import write.assets as assets


def configure():
    """Run the initialization"""

    config.write()
    javafile.write()
    assets.write()
