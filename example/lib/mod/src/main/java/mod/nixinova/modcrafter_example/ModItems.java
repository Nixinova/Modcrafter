package mod.nixinova.modcrafter_example;

import net.minecraft.block.Block;
import net.minecraft.item.BlockItem;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroup;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;

import mod.nixinova.modcrafter_example.Main;
import mod.nixinova.modcrafter_example.ModBlocks;
import mod.nixinova.modcrafter_example.ModTabs;

public class ModItems {

    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, Main.MODID);

    // Items:
    public static final Item HALF_ITEM = addItem(
        "half_item",
        new Item.Properties()
            .maxStackSize(32)
            .group(ModTabs.CUSTOM)
    );
    public static final Item REGULAR_ITEM = addItem(
        "regular_item",
        new Item.Properties()
            .maxStackSize(64)
            .group(ItemGroup.MISC)
    );
    public static final Item FULL_BLOCK = addItem(
        "full_block",
        ModBlocks.FULL_BLOCK,
        new Item.Properties()
            .maxStackSize(12)
            .group(ModTabs.CUSTOM)
    );

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
