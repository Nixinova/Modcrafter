package $PACKAGE;

import net.minecraft.block.Block;
import net.minecraft.item.BlockItem;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroup;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;

import $PACKAGE.Main;
import $PACKAGE.ModBlocks;
import $PACKAGE.ModTabs;

public class ModItems {

    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, Main.MODID);

    // Items:$ITEMS

    public static Item addItem(String name, Item.Properties properties) {
        Item item = new Item(properties);
        ITEMS.register(name, () -> item);
        return item;
    }

    public static BlockItem addItem(String name, Block block, Item.Properties properties) {
        BlockItem blockItem = new BlockItem(block, properties);
        ITEMS.register(name, () -> blockItem);
        return blockItem;
    }

    public static void addItems() {
        ITEMS.register(FMLJavaModLoadingContext.get().getModEventBus());
    }

}
