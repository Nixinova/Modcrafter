package $PACKAGE;

import net.minecraft.block.AbstractBlock;
import net.minecraft.block.Block;
import net.minecraft.block.Blocks;
import net.minecraft.block.SoundType;
import net.minecraft.block.material.Material;
import net.minecraft.item.BlockItem;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroup;
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
    }

    public static void addBlock(
        String name,
        boolean itemForm,
        boolean solid,
        Material material,
        float hardness,
        float resistance,
        SoundType sound,
        int stackSize, // blockItem only
        ItemGroup group // blockItem only
    ) {
        AbstractBlock.Properties blockProps = AbstractBlock.Properties
            .create(material)
            .hardnessAndResistance(hardness, resistance)
            .sound(sound)
            ;
        if (!solid) blockProps = blockProps.notSolid();

        Block block = new Block(blockProps);

        Item.Properties itemProps = new Item.Properties()
            .maxStackSize(stackSize)
            .group(group)
            ;

        BlockItem blockItem = new BlockItem(block, itemProps);

        BLOCKS.register(name, () -> block);
        if (itemForm) {
            ITEMS.register(name, () -> blockItem);
        }
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
        //Blocks:$BLOCKS
        BLOCKS.register(FMLJavaModLoadingContext.get().getModEventBus());
    }

    // List of items
    public static void addItems() {
        //Items:$ITEMS
        ITEMS.register(FMLJavaModLoadingContext.get().getModEventBus());
    }

}
