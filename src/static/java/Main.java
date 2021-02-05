package $PACKAGE;

import net.minecraftforge.fml.common.Mod;

import $PACKAGE.ModItems;
import $PACKAGE.ModBlocks;

@Mod(Main.MODID)
public class Main {

    public static final String MODID = "$MODID";

    public Main() {
        ModBlocks.addBlocks();
        ModItems.addItems();
    }

}
