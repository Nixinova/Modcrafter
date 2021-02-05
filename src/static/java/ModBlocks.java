package $PACKAGE;

import net.minecraft.block.AbstractBlock;
import net.minecraft.block.Block;
import net.minecraft.block.Blocks;
import net.minecraft.block.SoundType;
import net.minecraft.block.material.Material;
import net.minecraft.item.BlockItem;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;

import $PACKAGE.Main;
import $PACKAGE.ModItems;
import $PACKAGE.ModTabs;

public class ModBlocks {

    public static final DeferredRegister<Block> BLOCKS
        = DeferredRegister.create(ForgeRegistries.BLOCKS, Main.MODID);
    
    //Blocks:$BLOCKS

    public static Block addBlock(
        String name,
        boolean itemForm,
        boolean solid,
        Material material,
        float hardness,
        float resistance,
        SoundType sound,
        int stackSize, // block item only
        ItemGroup group // block item only
    ) {
        // Register block
        AbstractBlock.Properties blockProps = AbstractBlock.Properties.create(material)
            .hardnessAndResistance(hardness, resistance)
            .sound(sound)
            ;
        if (!solid) blockProps = blockProps.notSolid();
        Block block = new Block(blockProps);
        BLOCKS.register(name, () -> block);

        // Register block item
        Item.Properties itemProps = new Item.Properties()
            .maxStackSize(stackSize)
            .group(group)
            ;
        if (itemForm) {
            ModItems.ITEMS.register(name, () -> new BlockItem(block, itemProps));
        }

        return block;
    }

    public static void addBlocks() {
        BLOCKS.register(FMLJavaModLoadingContext.get().getModEventBus());
    }

}
