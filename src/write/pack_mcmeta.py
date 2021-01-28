"""Modify pack.mcmeta"""

import os
import re

import modfile

OUTPUT_FOLDER = 'gen/lib/'


def configure():
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
