"""Build commands"""

import sys
import os

args = sys.argv

commands = {
    "setup": """
        python src/download.py
      """,
    "main": """
        python src/__main__.py
      """,
    "jar": """
        python src/compile.py
      """,
    "compile": """
        cd bin
        && pyinstaller ../src/__main__.py
            --name Modcrafter
            --add-data ../src/static;static
            --clean
            --log-level WARN
            --noconfirm
            -F
      """,
}

script = commands[args[1]]
os.system(script.replace('\n', ''))
