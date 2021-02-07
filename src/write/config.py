"""Modify configuration files"""

import os
import re

from globals import *
import modfile


def write():
    """Run configuration"""

    pack_mcmeta()
    mods_toml()
    build_gradle()


def pack_mcmeta():
    """Configures pack.mcmeta"""

    FOLDER = OUTPUT_FOLDER + 'src/main/resources/'

    pack_mcmeta = FOLDER + 'pack.mcmeta'
    pack_mcmeta_temp = pack_mcmeta + '.temp'

    with open(pack_mcmeta, 'r') as read:
        with open(pack_mcmeta_temp, 'w') as write:
            for ln in read:

                if ln.find('"description"'):
                    desc = 'Resources for ' + modfile.get('name')
                    ln = re.sub(r'(^\s*"description":\s*).+$', rf'\1"{desc}",', ln)

                write.write(ln)

    os.remove(pack_mcmeta)
    os.rename(pack_mcmeta_temp, pack_mcmeta)


def mods_toml():
    """Configures mods.toml"""

    FOLDER = OUTPUT_FOLDER + 'src/main/resources/META-INF/'

    mods_toml = FOLDER + 'mods.toml'
    mods_toml_temp = mods_toml + '.temp'

    license_msg = modfile.get('license') or 'Unspecified'
    modid = modfile.get('modid')
    author = modfile.get('author')
    bugs = modfile.get('bugs')
    website = modfile.get('website')
    logo = modfile.get('logo')
    credit = modfile.get('credits')

    with open(mods_toml, 'r') as read:
        with open(mods_toml_temp, 'w') as write:

            for ln in read:

                if re.search(r'^\s*#', ln):
                    continue

                if re.search(r'^description', ln):
                    break

                ln = re.sub(r'\s*#.+$', '', ln)

                ln = re.sub(r'(^license=).+', rf'\1"{license_msg}"', ln)
                ln = re.sub(r'(^modId=).+', rf'\1"{modid}"', ln)
                ln = re.sub(r'(^authors=).+', author and rf'\1"{author}"' or '', ln)
                ln = re.sub(r'(^issue.+=).+', bugs and rf'\1"{bugs}"' or '', ln)
                ln = re.sub(r'(^.+URL=).+', website and rf'\1"{website}"' or '', ln)
                ln = re.sub(r'(^logoFile=).+', logo and rf'\1"{logo}"' or '', ln)
                ln = re.sub(r'(^credits=).+', credit and rf'\1"{credit}"' or '', ln)

                if not re.match(r'^\s*$', ln):
                    write.write(ln)

            desc = re.sub(r'\r\n', '\n', modfile.get("description"))
            write.write('description=' + f'"""{desc}"""')

    os.remove(mods_toml)
    os.rename(mods_toml_temp, mods_toml)


def build_gradle():
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
