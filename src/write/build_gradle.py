"""Modify build.gradle"""

import os
import re

import modfile

OUTPUT_FOLDER = 'gen/lib/'


def configure():
    """Configure build.gradle"""

    build_gradle = OUTPUT_FOLDER + 'build.gradle'
    build_gradle_temp = build_gradle + '.temp'

    with open(build_gradle, 'r') as gradle_read:
        with open(build_gradle_temp, 'w') as gradle_write:
            for ln in gradle_read:

                if re.search(r'^\s*//.+$', ln):
                    continue

                line = re.sub(r'\s+//.+$', '', ln.rstrip())

                line = re.sub(r"(?<=^version = )'1.0'$", f"'{modfile.get('version')}'", line)
                line = re.sub(r"(?<=^group = ).+$", f"'{modfile.get('package')}'", line)
                line = re.sub(r"(?<=^archivesBaseName = ).+$", f"'{modfile.get('modid')}'", line)
                
                line = line.replace('examplemod', modfile.get('modid'))

                gradle_write.write(line + '\n')

    os.remove(build_gradle)
    os.rename(build_gradle_temp, build_gradle)
