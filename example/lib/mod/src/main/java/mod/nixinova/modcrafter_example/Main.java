package mod.nixinova.modcrafter_example;

import net.minecraftforge.fml.common.Mod;

import mod.nixinova.modcrafter_example.ModItems;
import mod.nixinova.modcrafter_example.ModBlocks;

@Mod(Main.MODID)
public class Main {

    public static final String MODID = "modcrafter_example";

    public Main() {
        ModBlocks.addBlocks();
        ModItems.addItems();
    }

}
