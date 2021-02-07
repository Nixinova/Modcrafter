# Modcrafter

Modcrafter is a tool used to create and compile Minecraft Forge mods from a single configuration file.

## Install

Download Modcrafter from the attached exe file on the latest [release](https://github.com/Nixinova/Modcrafter/releases).
Alternatively, grab the live version of the exe from path `/bin/dist/Modcrafter.exe` of this repository.

## Usage

1. Copy the exe file into your mod directory.
2. Run it once to initialise the project.
3. Edit the `Modcrafter.yml` file to your liking.
4. Place any textures for your mod in the `/lib/textures/` folder.
5. When done, run `Modcrafter.exe` again. You will find your outputted mod file in `/lib/jars/`.
6. Place the outputted jar file in the `.minecraft/mods/` folder and load up Forge to play your mod!

## Build from source

Run `python run compile` to compile Modcrafter from this source code. Outputted exe is in `bin/dist/`.
