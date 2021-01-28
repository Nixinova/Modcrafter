"""Modcrafter"""

import download as mdk
import write as files
import compile as compiler
import modfile

modfile.read()
mdk.download()
files.configure()
compiler.run()
