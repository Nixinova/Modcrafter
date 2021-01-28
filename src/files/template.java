package $PACKAGE;

import net.minecraft.block.Block;
import net.minecraft.block.Blocks;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroup;
import net.minecraft.block.material.Material;
import net.minecraftforge.fml.RegistryObject;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;

@Mod(Main.MODID)
public class Main {

    public static final String MODID = "$MODID";

    public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, MODID);
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, MODID);

    public Main() {
        addBlocks();
        addItems();
        BLOCKS.register(FMLJavaModLoadingContext.get().getModEventBus());
        ITEMS.register(FMLJavaModLoadingContext.get().getModEventBus());
    }

    public static void addBlock(String name, Material material) {
        RegistryObject<Block> newBlock = BLOCKS.register(
            name,
            () -> new Block(Block.Properties.create(material))
        );
    }

    public static void addItem(String name, ItemGroup group) {
        RegistryObject<Item> newItem = ITEMS.register(
            name,
            () -> new Item(new Item.Properties().group(group))
        );
    }

    // List of blocks
    public static void addBlocks() {
        addBlock("a_custom_block", Material.ROCK);
    }

    // List of items
    public static void addItems() {
        addItem("a_custom_item", ItemGroup.MATERIALS);
    }

}
