"""Configure build.gradle"""

import os
import re
import yaml

import files.modfile as modfile

OUTPUT_FOLDER = 'gen/lib/'

def configure():
    
    modfile_content = modfile.default()
    if os.path.exists('Modfile'):
        with open('Modfile', 'r') as file:
            file_content = yaml.safe_load(file)
            if file_content:
                modfile_content = file_content
    else:
        with open('Modfile', 'w') as file:
            yaml.dump(modfile_content, file)
            
    build_gradle = OUTPUT_FOLDER + 'build.gradle'
    build_gradle_temp = OUTPUT_FOLDER + 'build.gradle.temp'
            
    with open(build_gradle, 'r') as gradle_read:
        with open(build_gradle_temp, 'w') as gradle_write:
            for ln in gradle_read:
                
                if re.search(r'^\s*//.+$', ln): continue
                
                line = re.sub(r'\s+//.+$', '', ln.rstrip())
                
                version = modfile_content['version']
                authorID = re.sub(r"[^\w\d]", '', modfile_content['author']).lower()
                modID = re.sub(r"[^\w\d]", '', modfile_content['name']).lower()
                group = f"com.{authorID}.{modID}"
                
                line = line.replace("version = '1.0'", f"version = '{version}'")
                line = line.replace("group = 'com.yourname.modid'", f"group = '{group}'")
                line = line.replace("archivesBaseName = 'modid'", f"archivesBaseName = '{modID}'")

                if ln != line or not ln:
                    gradle_write.write(line + '\n')
                    
    os.remove(build_gradle)
    os.rename(build_gradle_temp, build_gradle)
