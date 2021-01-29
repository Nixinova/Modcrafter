package $PACKAGE;

import net.minecraft.block.Block;
import net.minecraft.block.Blocks;
import net.minecraft.block.SoundType;
import net.minecraft.item.BlockItem;
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

    public static Block addBlock(
        String name,
        Material material,
        float hardness,
        SoundType sound,
        int light
    ) {
        Block newBlock = new Block(Block.Properties
            .create(material)
            .hardnessAndResistance(hardness)
            //#.lightValue(light)
            .sound(sound)
            .notSolid()
        );
        BLOCKS.register(name, () -> newBlock);
        return newBlock;
    }

    public static void addBlockItem(
        String name,
        Material material,
        float hardness,
        SoundType sound,
        int light,
        int stackSize,
        ItemGroup group
    ) {
        Block newBlock = addBlock(name, material, hardness, sound, light);
        RegistryObject<Item> itemBlock = ITEMS.register(
            name,
            () -> new BlockItem(newBlock, new Item.Properties().maxStackSize(stackSize).group(group))
        );
    }

    public static void addItem(
        String name,
        int stackSize,
        ItemGroup group
    ) {
        RegistryObject<Item> newItem = ITEMS.register(
            name,
            () -> new Item(new Item.Properties().maxStackSize(stackSize).group(group))
        );
    }

    // List of blocks
    public static void addBlocks() {
        //#$BLOCKS
    }

    // List of items
    public static void addItems() {
        //#$ITEMS
    }

}
