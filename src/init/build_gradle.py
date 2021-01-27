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

                version = modfile.get('version')
                authorID = re.sub(r"[^\w\d]", '', modfile.get('author'))
                modID = modfile.get('id') or modfile.get('name').lower().replace(' ', '')
                group = f"com.{authorID.lower()}.{modID.lower()}"

                line = line.replace("(?<=version = )'1.0'", f"'{version}'")
                line = line.replace(r"(?<=group = ).+$", f"'{group}'")
                line = line.replace(r"(?<=archivesBaseName = ).=$", f"'{modID}'")

                if ln != line or not ln:
                    gradle_write.write(line + '\n')

    os.remove(build_gradle)
    os.rename(build_gradle_temp, build_gradle)
