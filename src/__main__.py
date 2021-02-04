"""Modcrafter"""

import modfile
import download as mdk
import write as files
import compile as compiler

print("--- Modcrafter ---\n")

modfile.read()
mdk.download()
files.configure()
compiler.run()
