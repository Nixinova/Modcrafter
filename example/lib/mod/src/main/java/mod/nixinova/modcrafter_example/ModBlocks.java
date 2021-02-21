package mod.nixinova.modcrafter_example;

import net.minecraft.block.AbstractBlock;
import net.minecraft.block.Block;
import net.minecraft.block.Blocks;
import net.minecraft.block.SoundType;
import net.minecraft.block.material.Material;
import net.minecraft.block.material.MaterialColor;
import net.minecraft.item.BlockItem;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;

import mod.nixinova.modcrafter_example.Main;
import mod.nixinova.modcrafter_example.ModItems;
import mod.nixinova.modcrafter_example.ModTabs;

public class ModBlocks {

    public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, Main.MODID);

    // Blocks:
    public static final Block EMPTY_BLOCK = addBlock(
        "empty_block",
        new Block(AbstractBlock.Properties
            .create(Material.ROCK, MaterialColor.STONE)
            .zeroHardnessAndResistance()
            .sound(SoundType.METAL)
            .doesNotBlockMovement()
        )
    );
    public static final Block FULL_BLOCK = addBlock(
        "full_block",
        new Block(AbstractBlock.Properties
            .create(Material.ROCK, MaterialColor.STONE)
            .hardnessAndResistance(1.5f, 6f)
            .sound(SoundType.METAL)
            .notSolid()
        )
    );

    private static Block addBlock(String name, Block block) {
        BLOCKS.register(name, () -> block);
        return block;
    }

    public static void addBlocks() {
        BLOCKS.register(FMLJavaModLoadingContext.get().getModEventBus());
    }

}
