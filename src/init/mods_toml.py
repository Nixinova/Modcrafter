"""Modify mods.toml"""

import os
import re

import modfile

OUTPUT_FOLDER = 'gen/lib/'


def configure():
    """Configures mods.toml"""

    FOLDER = OUTPUT_FOLDER + 'src/main/resources/META-INF/'

    mods_toml = FOLDER + 'mods.toml'
    mods_toml_temp = mods_toml + '.temp'

    with open(mods_toml, 'r') as read:
        with open(mods_toml_temp, 'w') as write:
            for ln in read:

                if re.search(r'^\s*#', ln):
                    continue

                if re.search(r'^description', ln):
                    break

                ln = re.sub(r'\s*#.+$', '', ln)

                license_msg = modfile.get('license') or 'Unspecified'
                modid = modfile.get('id') or modfile.get('name').lower().replace(' ', '')
                author = modfile.get('author')
                bugs = modfile.get('bugs')
                website = modfile.get('website')
                logo = modfile.get('logo')
                credit = modfile.get('credits')

                ln = re.sub(r'(^license=).+$', rf'\1"{license_msg}"', ln)
                ln = re.sub(r'(^modId=).+', rf'\1"{modid}"', ln)
                ln = re.sub(r'(^authors=).+', author and rf'\1"{author}"' or '', ln)
                ln = re.sub(r'(^issue.+=).+', bugs and rf'\1"{bugs}"' or '', ln)
                ln = re.sub(r'(^.+URL=).+', website and rf'\1"{website}"' or '', ln)
                ln = re.sub(r'(^logoFile=).+', logo and rf'\1"{logo}"' or '', ln)
                ln = re.sub(r'(^credits=).+', credit and rf'\1"{credit}"' or '', ln)

                if not re.match(r'^\s*$', ln):
                    write.write(ln)
            write.write('description=' + f'"""\n{modfile.get("description")}\n"""')

    os.remove(mods_toml)
    os.rename(mods_toml_temp, mods_toml)
