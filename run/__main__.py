"""Build commands"""

import sys
import os

commands = {
    "setup": """
        python src/download.py
        """,
    "main": """
        python src/__main__.py
        """,
    "gui": """
        cd example
        &&
        python ../src/app.py
        """,
    "jar": """
        python src/compile.py
        """,
    "compile": """
        cd bin
        &&
        pyinstaller ../src/__main__.py
            --name Modcrafter
            --add-data ../src/static;static
            --add-data ../src/gui;gui
            --clean
            --log-level WARN
            --noconfirm
            -F
        """,
}

script = commands[sys.argv[1]]
os.system(script.replace('\n', ''))
