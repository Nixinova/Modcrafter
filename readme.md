# Modcrafter

Modcrafter is a tool used to create and compile Minecraft Forge mods using a simple GUI.
No Java knowledge or IDE required!

## Download

Download Modcrafter from the attached exe file on the latest [release](https://github.com/Nixinova/Modcrafter/releases).
Alternatively, grab the live version of the exe from path `/bin/dist/Modcrafter.exe` of this repository.

## Usage

1. Copy the exe into the directory you will be using for your mod.
1. Run the exe and use the GUI to configure your mod.
1. When adding textures, make sure to add the relevant files into folder `lib/textures/`.
1. When done configuring, click "Generate" and the mod will start compiling. You will find your outputted mod file in `/lib/jars/`.
1. Place the outputted jar file in your `.minecraft/mods/` folder and load up Forge to play your mod!

## Build from source

Run `python run compile` to compile Modcrafter from this source code. Outputted exe is in `bin/dist/`.
