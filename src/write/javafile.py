"""Write to Java file"""

import os

import modfile

OUTPUT_FOLDER = 'gen/lib/'


def write():
    """Write to Java file"""

    PACKAGE = modfile.get('package')
    FOLDER = OUTPUT_FOLDER + 'src/main/java/' + PACKAGE.replace('.', '/') + '/'
    os.makedirs(FOLDER)

    fc = ''
    with open('src/files/template.java', 'r') as file:
        fc = file.read()

    fc = fc.replace('$PACKAGE', modfile.get('package'))
    fc = fc.replace('$MODID', modfile.get('modid'))

    with open(FOLDER + 'Main.java', 'w') as file:
        file.write(fc)
