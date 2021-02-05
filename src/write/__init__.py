"""Initializes project"""

import write.config as config
import write.java as java
import write.assets as assets


def configure():
    """Run the initialization"""

    config.write()
    java.write()
    assets.write()
