const $ = q => document.querySelector(q);
const $$ = q => document.querySelectorAll(q);

let blockCount = 0, itemCount = 0;

const datalists = {
    mapDisplays: [
        "adobe", "air", "black", "black_terracotta", "blue", "blue_terracotta", "brown", "brown_terracotta", "clay", "crimson_hyphae", "crimson_nylium", "crimson_stem", "cyan", "cyan_terracotta", "diamond", "dirt", "emerald", "foliage", "gold", "grass", "gray", "gray_terracotta", "green", "green_terracotta", "ice", "iron", "lapis", "light_blue", "light_blue_terracotta", "light_gray", "light_gray_terracotta", "lime", "lime_terracotta", "magenta", "magenta_terracotta", "netherrack", "obsidian", "orange_terracotta", "pink", "pink_terracotta", "purple", "purple_terracotta", "quartz", "red", "red_terracotta", "sand", "snow", "stone", "tnt", "warped_hyphae", "warped_nylium", "warped_stem", "warped_wart", "water", "white_terracotta", "wood", "wool", "yellow", "yellow_terracotta"
    ],
    inventoryTabs: [
        "brewing", "building_blocks", "combat", "decorations", "food", "hotbar", "inventory", "materials", "misc", "redstone", "search", "tools", "transportation"
    ],
    materials: [
        "air", "anvil", "barrier", "cactus", "cake", "carpet", "circuits", "clay", "cloth", "coral", "crafted_snow", "dragon_egg", "fire", "glass", "gourd", "grass", "ground", "ice", "iron", "lava", "leaves", "packed_ice", "piston", "plants", "portal", "redstone_light", "rock", "sand", "snow", "sponge", "tnt", "vine", "water", "web", "wood"
    ],
    sounds: [
        "ancient_debris", "anvil", "bamboo", "bamboo_sapling", "basalt", "bone", "chain", "cloth", "coral", "crop", "fungus", "gilded_blackstone", "glass", "ground", "honey", "hyphae", "ladder", "lantern", "lily_pads", "lodestone", "metal", "nether_brick", "nether_gold", "nether_ore", "nether_sprout", "nether_vine", "nether_vine_lower_pitch", "nether_wart", "netherite", "netherrack", "nylium", "plant", "root", "sand", "scaffolding", "shroomlight", "slime", "snow", "soul_sand", "soul_soil", "stem", "stone", "sweet_berry_bush", "vine", "wart", "wet_grass", "wood"
    ]
};

function add(type) {
    let count = type === 'block' ? ++blockCount : ++itemCount;

    let templateContent = $(`#${type}s-template`).innerHTML
        .replace(RegExp(`(?<=new_${type})`), count)
        .replace(/="(items|blocks)(?=\.)/g, '$&' + count)

    let newElem = document.createElement('div');
    newElem.setAttribute('class', type);
    newElem.setAttribute('data-id', count);
    newElem.innerHTML = templateContent;

    $(`#${type}s`).appendChild(newElem);
}

function remove(elem) {
    elem.parentNode.parentNode.removeChild(elem.parentNode);
}

function toggle(elem) {
    elem.classList.toggle('yes');
    elem.classList.toggle('no');
}

function setTemplate(type, elem) {
    let template = elem.value;
    let id = elem.parentNode.parentNode.getAttribute('data-id');
    let parent = `[data-id="${id}"]`;

    const getElem = id => $(`${parent} [name*="${id}"]`);
    const remove = (...ids) => {
        for (id of ids) {
            getElem(id)?.parentNode.classList.add('hide');
        }
    }
    const checkboxes = (...arr) => {
        for (s of arr) {
            let parts = s.split('=');
            getElem(parts[0]).checked = Boolean(parts[1]);
        }
    }

    $$(`${parent} p`).forEach(elem => elem.classList.remove('hide'));
    checkboxes('itemForm=false');

    if (template === 'world-only') {
        checkboxes('itemForm=true');
        remove('inventoryTab', 'stackSize', 'itemForm');
    }
}

function addDatalists() {
    for (let list of Object.keys(datalists)) {
        let datalist = document.createElement('datalist');
        datalist.id = list;
        for (let item of datalists[list]) {
            datalist.innerHTML += `<option value="${item}">`;
        }
        document.body.appendChild(datalist);
    }
}

function validate(type, elem) {
    let valid = datalists[type]?.includes(elem.value.toLowerCase());
    elem.classList[valid ? 'remove' : 'add']('invalid');
}

function submitted() {
    let logger = $('#logging');
    logger.classList.remove('hide');
    setInterval(function () {
        dots = $('#logging_dots');
        dots.innerText += '.';
        if (dots.innerText.length > 3) dots.innerText = '';
    }, 500);
}

document.addEventListener('DOMContentLoaded', function () {
    addDatalists();
});
