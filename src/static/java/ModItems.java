package $PACKAGE;

import net.minecraft.item.Item;
import net.minecraft.item.ItemGroup;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;

import $PACKAGE.Main;
import $PACKAGE.ModBlocks;
import $PACKAGE.ModTabs;

public class ModItems {

    public static final DeferredRegister<Item> ITEMS
        = DeferredRegister.create(ForgeRegistries.ITEMS, Main.MODID);

    //Items:$ITEMS

    public static Item addItem(
        String name,
        int stackSize,
        ItemGroup group
    ) {
        Item.Properties props = new Item.Properties()
            .maxStackSize(stackSize)
            .group(group)
            ;
        Item item = new Item(props);
        ITEMS.register(name,  () -> item);
        return item;
    }

    public static void addItems() {
        ITEMS.register(FMLJavaModLoadingContext.get().getModEventBus());
    }

}
