package mod.nixinova.modcrafter_example;

import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;

import mod.nixinova.modcrafter_example.ModBlocks;
import mod.nixinova.modcrafter_example.ModItems;

public class ModTabs {

    //Inventory tabs:
	
    public static final ItemGroup CUSTOM = new ItemGroup(12, "custom") {
        public ItemStack createIcon() {
            return new ItemStack(ModItems.HALF_ITEM);
        }
    };

}
