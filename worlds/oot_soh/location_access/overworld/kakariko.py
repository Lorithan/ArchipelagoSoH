from typing import TYPE_CHECKING

from ...Enums import *
from ...LogicHelpers import *

if TYPE_CHECKING:
    from worlds.oot_soh import SohWorld


class EventLocations(str, Enum):
    KAKARIKO_GATE_GUARD = "Kakariko Gate Guard"
    KAKARIKO_ROCK = "Kakariko Rock"
    KAKARIKO_ADULT_TALON = "Kakariko Adult Talon"
    KAKARIKO_WINDMILL_PHONOGRAM_MAN = "Kakariko Windmill Phonogram Man"


class LocalEvents(str, Enum):
    WAKE_UP_ADULT_TALON = "Wake Up Talon As Adult"
    KAKARIKO_GATE_OPEN = "Kakariko Gate Open"


def set_region_rules(world: "SohWorld") -> None:
    # Kakariko Village
    # Events
    add_events(Regions.KAKARIKO_VILLAGE, world, [
        (EventLocations.KAKARIKO_ROCK, Events.CAN_ACCESS_BUGS, lambda bundle: True),
        (EventLocations.KAKARIKO_GATE_GUARD, LocalEvents.KAKARIKO_GATE_OPEN,
         lambda bundle: is_child(bundle) and has_item(Items.ZELDAS_LETTER, bundle)),
        (EventLocations.KAKARIKO_GATE_GUARD, Events.BORROW_SKULL_MASK,
         lambda bundle: is_child(bundle) and has_item(Events.CAN_BORROW_MASKS, bundle) and has_item(Items.CHILD_WALLET,
                                                                                                    bundle)),
    ])
    # Locations
    add_locations(Regions.KAKARIKO_VILLAGE, world, [
        (Locations.SHEIK_IN_KAKARIKO,
         lambda bundle: is_adult(bundle) and has_item(Items.FOREST_MEDALLION, bundle) and has_item(
             Items.FIRE_MEDALLION, bundle) and has_item(Items.WATER_MEDALLION, bundle)),
        (Locations.KAK_ANJU_AS_CHILD, lambda bundle: is_child(bundle) and at_day(bundle)),
        (Locations.KAK_ANJU_AS_ADULT, lambda bundle: is_adult(bundle) and at_day(bundle)),
        (Locations.KAK_TRADE_POCKET_CUCCO, lambda bundle: is_adult(bundle) and at_day(bundle) and (
                can_use(Items.POCKET_EGG, bundle) and has_item(LocalEvents.WAKE_UP_ADULT_TALON, bundle))),
        (Locations.KAK_GS_HOUSE_UNDER_CONSTRUCTION, lambda bundle: is_child(bundle) and can_get_nighttime_gs(bundle)),
        (Locations.KAK_GS_SKULLTULA_HOUSE, lambda bundle: is_child(bundle) and can_get_nighttime_gs(bundle)),
        (Locations.KAK_GS_GUARDS_HOUSE, lambda bundle: is_child(bundle) and can_get_nighttime_gs(bundle)),
        (Locations.KAK_GS_TREE,
         lambda bundle: is_child(bundle) and can_get_nighttime_gs(bundle) and can_bonk_trees(bundle)),
        (Locations.KAK_GS_WATCHTOWER, lambda bundle: is_child(bundle) and (
                can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA, EnemyDistance.LONGSHOT) or (
                can_do_trick("RT Kak Tower GS", bundle) and can_jump_slash(bundle)) and can_get_nighttime_gs(bundle))),
        (Locations.KAK_NEAR_POTION_SHOP_POT1, lambda bundle: is_child(bundle) and can_break_pots(bundle)),
        (Locations.KAK_NEAR_POTION_SHOP_POT2, lambda bundle: is_child(bundle) and can_break_pots(bundle)),
        (Locations.KAK_NEAR_POTION_SHOP_POT3, lambda bundle: is_child(bundle) and can_break_pots(bundle)),
        (Locations.KAK_NEAR_IMPAS_HOUSE_POT1, lambda bundle: is_child(bundle) and can_break_pots(bundle)),
        (Locations.KAK_NEAR_IMPAS_HOUSE_POT2, lambda bundle: is_child(bundle) and can_break_pots(bundle)),
        (Locations.KAK_NEAR_IMPAS_HOUSE_POT3, lambda bundle: is_child(bundle) and can_break_pots(bundle)),
        (Locations.KAK_NEAR_GUARDS_HOUSE_POT1, lambda bundle: is_child(bundle) and can_break_pots(bundle)),
        (Locations.KAK_NEAR_GUARDS_HOUSE_POT2, lambda bundle: is_child(bundle) and can_break_pots(bundle)),
        (Locations.KAK_NEAR_GUARDS_HOUSE_POT3, lambda bundle: is_child(bundle) and can_break_pots(bundle)),
        (Locations.KAK_TREE_GRASS1, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_TREE_GRASS2, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_TREE_GRASS3, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_TREE_GRASS4, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_TREE_GRASS5, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_NEAR_GRAVEYARD_GRASS1, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_NEAR_GRAVEYARD_GRASS2, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_NEAR_GRAVEYARD_GRASS3, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_NEAR_OPEN_GROTTO_ADULT_CRATE1, lambda bundle: is_adult(bundle) and can_break_crates(bundle)),
        (Locations.KAK_NEAR_OPEN_GROTTO_ADULT_CRATE2, lambda bundle: is_adult(bundle) and can_break_crates(bundle)),
        (Locations.KAK_NEAR_OPEN_GROTTO_ADULT_CRATE3, lambda bundle: is_adult(bundle) and can_break_crates(bundle)),
        (Locations.KAK_NEAR_OPEN_GROTTO_ADULT_CRATE4, lambda bundle: is_adult(bundle) and can_break_crates(bundle)),
        (Locations.KAK_NEAR_POTION_SHOP_ADULT_CRATE, lambda bundle: is_adult(bundle) and can_break_crates(bundle)),
        (Locations.KAK_NEAR_SHOOTING_GALLERY_ADULT_CRATE, lambda bundle: is_adult(bundle) and can_break_crates(bundle)),
        (Locations.KAK_NEAR_BOARDING_HOUSE_ADULT_CRATE1, lambda bundle: is_adult(bundle) and can_break_crates(bundle)),
        (Locations.KAK_NEAR_BOARDING_HOUSE_ADULT_CRATE2, lambda bundle: is_adult(bundle) and can_break_crates(bundle)),
        (Locations.KAK_BEHIND_GS_HOUSE_ADULT_CRATE, lambda bundle: is_adult(bundle) and can_break_crates(bundle)),
        (Locations.KAK_NEAR_GRAVEYARD_CHILD_CRATE, lambda bundle: is_child(bundle) and can_break_crates(bundle)),
        (Locations.KAK_NEAR_WINDMILL_CHILD_CRATE, lambda bundle: is_child(bundle) and can_break_crates(bundle)),
        (Locations.KAK_NEAR_FENCE_CHILD_CRATE, lambda bundle: is_child(bundle) and can_break_crates(bundle)),
        (Locations.KAK_NEAR_BOARDING_HOUSE_CHILD_CRATE, lambda bundle: is_child(bundle) and can_break_crates(bundle)),
        (Locations.KAK_NEAR_BAZAAR_CHILD_CRATE, lambda bundle: is_child(bundle) and can_break_crates(bundle)),
    ])
    # Connections
    connect_regions(Regions.KAKARIKO_VILLAGE, world, [
        (Regions.HYRULE_FIELD, lambda bundle: True),
        (Regions.KAK_CARPENTER_BOSS_HOUSE, lambda bundle: can_open_overworld_door(Items.BOSS_HOUSE_KEY, bundle)),
        (Regions.KAK_HOUSE_OF_SKULLTULA, lambda bundle: can_open_overworld_door(Items.SKULLTULA_HOUSE_KEY, bundle)),
        (Regions.KAK_IMPAS_HOUSE, lambda bundle: can_open_overworld_door(Items.IMPAS_HOUSE_KEY, bundle)),
        (Regions.KAK_WINDMILL, lambda bundle: can_open_overworld_door(Items.WINDMILL_KEY, bundle)),
        (Regions.KAK_BAZAAR,
         lambda bundle: is_adult(bundle) and at_day(bundle) and can_open_overworld_door(Items.KAK_BAZAAR_KEY, bundle)),
        (Regions.KAK_SHOOTING_GALLERY,
         lambda bundle: is_adult(bundle) and at_day(bundle) and can_open_overworld_door(Items.KAK_SHOOTING_GALLERY_KEY,
                                                                                        bundle)),
        (Regions.KAK_WELL,
         lambda bundle: is_adult(bundle) or has_item(Events.DRAIN_WELL, bundle) or can_use(Items.IRON_BOOTS,
                                                                                           bundle) or (
                                can_do_trick("RT Bottom of the Well Navi Dive", bundle) and is_child(
                            bundle) and has_item(Items.BRONZE_SCALE, bundle) and can_jump_slash(bundle))),
        (Regions.KAK_POTION_SHOP_FRONT,
         lambda bundle: (at_day(bundle) or is_child(bundle)) and can_open_overworld_door(
             Items.KAK_POTION_SHOP_KEY, bundle)),
        (Regions.KAK_REDEAD_GROTTO, lambda bundle: can_open_bomb_grotto(bundle)),
        (Regions.KAK_IMPAS_LEDGE, lambda bundle: (is_child(bundle) and at_day(bundle)) or (
                is_adult(bundle) and can_do_trick("RT Visible Collision", bundle))),
        (Regions.KAK_WATCHTOWER,
         lambda bundle: is_adult(bundle) or at_day(bundle) or can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA,
                                                                             EnemyDistance.LONGSHOT) or can_do_trick(
             "RT Kak Tower GS", bundle) and can_jump_slash(bundle)),
        (Regions.KAK_ROOFTOP,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) or can_do_trick("RT Kak Man on Roof", bundle) and is_adult(
             bundle)),
        (Regions.KAK_IMPAS_ROOFTOP,
         lambda bundle: can_use(Items.HOOKSHOT, bundle) or can_do_trick("RT Kak Rooftop", bundle) and can_use(
             Items.HOVER_BOOTS, bundle)),
        (Regions.THE_GRAVEYARD, lambda bundle: True),
        (Regions.KAK_BEHIND_GATE,
         lambda bundle: is_adult(bundle) or has_item(LocalEvents.KAKARIKO_GATE_OPEN, bundle)),
        (Regions.KAK_BACKYARD, lambda bundle: is_adult(bundle) or at_day(bundle)),
    ])

    # Kak Impas Ledge
    # Connections
    connect_regions(Regions.KAK_IMPAS_LEDGE, world, [
        (Regions.KAK_IMPAS_HOUSE_BACK, lambda bundle: True),
        (Regions.KAKARIKO_VILLAGE, lambda bundle: True),
    ])

    # Kak Impas Rooftop
    # Locations
    add_locations(Regions.KAK_IMPAS_ROOFTOP, world, [
        (Locations.KAK_GS_ABOVE_IMPAS_HOUSE,
         lambda bundle: is_adult(bundle) and can_get_nighttime_gs(bundle) and can_kill_enemy(bundle,
                                                                                             Enemies.GOLD_SKULLTULA)),
    ])
    # Connections
    connect_regions(Regions.KAK_IMPAS_ROOFTOP, world, [
        (Regions.KAK_IMPAS_LEDGE, lambda bundle: True),
        (Regions.KAKARIKO_VILLAGE, lambda bundle: True),
    ])

    # Kak Watchtower
    # Locations
    add_locations(Regions.KAK_WATCHTOWER, world, [
        (Locations.KAK_GS_WATCHTOWER,
         lambda bundle: is_child(bundle) and can_use(Items.DINS_FIRE, bundle) and can_get_nighttime_gs(bundle)),
    ])
    # Connections
    connect_regions(Regions.KAK_WATCHTOWER, world, [
        (Regions.KAKARIKO_VILLAGE, lambda bundle: True),
        (Regions.KAK_ROOFTOP, lambda bundle: can_do_trick("RT Kak Man On Roof", bundle) and is_child(bundle)),
    ])

    # Kak Rooftop
    # Locations
    add_locations(Regions.KAK_ROOFTOP, world, [
        (Locations.KAK_MAN_ON_ROOF, lambda bundle: True),
    ])
    # Connections
    connect_regions(Regions.KAK_ROOFTOP, world, [
        (Regions.KAK_BACKYARD, lambda bundle: True),
        (Regions.KAKARIKO_VILLAGE, lambda bundle: True),
    ])

    # Kak Backyard
    # Locations
    add_locations(Regions.KAK_BACKYARD, world, [
        (Locations.KAK_NEAR_MEDICINE_SHOP_POT1, lambda bundle: is_child(bundle) and can_break_pots(bundle)),
        (Locations.KAK_NEAR_MEDICINE_SHOP_POT2, lambda bundle: is_child(bundle) and can_break_pots(bundle)),
    ])
    # Connections
    connect_regions(Regions.KAK_BACKYARD, world, [
        (Regions.KAKARIKO_VILLAGE, lambda bundle: True),
        (Regions.KAK_OPEN_GROTTO, lambda bundle: True),
        (Regions.KAK_GRANNYS_POTION_SHOP,
         lambda bundle: is_adult(bundle) and can_open_overworld_door(Items.GRANNYS_POTION_SHOP_KEY, bundle)),
        (Regions.KAK_POTION_SHOP_BACK,
         lambda bundle: is_adult(bundle) and at_day(bundle) and can_open_overworld_door(Items.GRANNYS_POTION_SHOP_KEY,
                                                                                        bundle)),
    ])

    # Kak Carpenter Boss House
    # Events
    add_events(Regions.KAK_CARPENTER_BOSS_HOUSE, world, [
        (EventLocations.KAKARIKO_ADULT_TALON, LocalEvents.WAKE_UP_ADULT_TALON,
         lambda bundle: is_adult(bundle) and can_use(Items.POCKET_EGG, bundle)),
    ])
    # Connections
    connect_regions(Regions.KAK_CARPENTER_BOSS_HOUSE, world, [
        (Regions.KAKARIKO_VILLAGE, lambda bundle: True),
    ])

    # Kak House of Skulltula
    # Locations
    add_locations(Regions.KAK_HOUSE_OF_SKULLTULA, world, [
        (Locations.KAK_10_GOLD_SKULLTULA_REWARD, lambda bundle: has_item(Items.GOLD_SKULLTULA_TOKEN, bundle, 10)),
        (Locations.KAK_20_GOLD_SKULLTULA_REWARD, lambda bundle: has_item(Items.GOLD_SKULLTULA_TOKEN, bundle, 20)),
        (Locations.KAK_30_GOLD_SKULLTULA_REWARD, lambda bundle: has_item(Items.GOLD_SKULLTULA_TOKEN, bundle, 30)),
        (Locations.KAK_40_GOLD_SKULLTULA_REWARD, lambda bundle: has_item(Items.GOLD_SKULLTULA_TOKEN, bundle, 40)),
        (Locations.KAK_50_GOLD_SKULLTULA_REWARD, lambda bundle: has_item(Items.GOLD_SKULLTULA_TOKEN, bundle, 50)),
    ])
    # Connections
    connect_regions(Regions.KAK_HOUSE_OF_SKULLTULA, world, [
        (Regions.KAKARIKO_VILLAGE, lambda bundle: True),
    ])

    # Kak Impas House
    # Locations
    add_locations(Regions.KAK_IMPAS_HOUSE, world, [
        (Locations.KAK_IMPAS_HOUSE_COW, lambda bundle: can_play_song(bundle, Items.EPONAS_SONG)),
    ])
    # Connections
    connect_regions(Regions.KAK_IMPAS_HOUSE, world, [
        (Regions.KAKARIKO_VILLAGE, lambda bundle: True),
    ])

    # Kak Impas House Back
    # Locations
    add_locations(Regions.KAK_IMPAS_HOUSE_BACK, world, [
        (Locations.KAK_IMPAS_HOUSE_FREESTANDING_PO_H, lambda bundle: True),
        (Locations.KAK_IMPAS_HOUSE_COW, lambda bundle: can_play_song(bundle, Items.EPONAS_SONG)),
    ])
    # Connections
    connect_regions(Regions.KAK_IMPAS_HOUSE_BACK, world, [
        (Regions.KAK_IMPAS_LEDGE, lambda bundle: True),
    ])

    # Kak Windmill
    # Events
    add_events(Regions.KAK_WINDMILL, world, [
        (EventLocations.KAKARIKO_WINDMILL_PHONOGRAM_MAN, Events.DRAIN_WELL,
         lambda bundle: is_child(bundle) and can_play_song(bundle, Items.SONG_OF_STORMS)),
    ])
    # Locations
    add_locations(Regions.KAK_WINDMILL, world, [
        (Locations.KAK_WINDMILL_FREESTANDING_PO_H,
         lambda bundle: can_use(Items.BOOMERANG, bundle) or has_item(Events.DAMPES_WINDMILL_ACCESS, bundle) or (
                 is_adult(bundle) and can_do_trick("RT Kak Adult Windmill POH", bundle)) or (
                                is_child(bundle) and can_jump_slash_except_hammer(bundle) and can_do_trick(
                            "RT Kak Child Windmill POH", bundle))),
        (Locations.SONG_FROM_WINDMILL,
         lambda bundle: is_adult(bundle) and has_item(Items.FAIRY_OCARINA, bundle))
    ])
    # Connections
    connect_regions(Regions.KAK_WINDMILL, world, [
        (Regions.KAKARIKO_VILLAGE, lambda bundle: True),
    ])

    # Kak Bazaar
    # Locations
    add_locations(Regions.KAK_BAZAAR, world, [
        (Locations.KAK_BAZAAR_ITEM1, lambda bundle: True),
        (Locations.KAK_BAZAAR_ITEM2, lambda bundle: True),
        (Locations.KAK_BAZAAR_ITEM3, lambda bundle: True),
        (Locations.KAK_BAZAAR_ITEM4, lambda bundle: True),
        (Locations.KAK_BAZAAR_ITEM5, lambda bundle: True),
        (Locations.KAK_BAZAAR_ITEM6, lambda bundle: True),
        (Locations.KAK_BAZAAR_ITEM7, lambda bundle: True),
        (Locations.KAK_BAZAAR_ITEM8, lambda bundle: True),
    ])
    connect_regions(Regions.KAK_BAZAAR, world, [
        (Regions.KAKARIKO_VILLAGE, lambda bundle: True),
    ])

    # Kak Shooting Gallery
    # Locations
    add_locations(Regions.KAK_SHOOTING_GALLERY, world, [
        (Locations.KAK_SHOOTING_GALLERY_REWARD, lambda bundle: has_item(Items.CHILD_WALLET, bundle)),
    ])
    # Connections
    connect_regions(Regions.KAK_SHOOTING_GALLERY, world, [
        (Regions.KAKARIKO_VILLAGE, lambda bundle: True),
    ])

    # Kak Potion Shop Front
    # Locations
    add_locations(Regions.KAK_POTION_SHOP_FRONT, world, [
        (Locations.KAK_POTION_SHOP_ITEM1, lambda bundle: is_adult(bundle)),
        (Locations.KAK_POTION_SHOP_ITEM2, lambda bundle: is_adult(bundle)),
        (Locations.KAK_POTION_SHOP_ITEM3, lambda bundle: is_adult(bundle)),
        (Locations.KAK_POTION_SHOP_ITEM4, lambda bundle: is_adult(bundle)),
        (Locations.KAK_POTION_SHOP_ITEM5, lambda bundle: is_adult(bundle)),
        (Locations.KAK_POTION_SHOP_ITEM6, lambda bundle: is_adult(bundle)),
        (Locations.KAK_POTION_SHOP_ITEM7, lambda bundle: is_adult(bundle)),
        (Locations.KAK_POTION_SHOP_ITEM8, lambda bundle: is_adult(bundle)),
    ])
    # Connections
    connect_regions(Regions.KAK_POTION_SHOP_FRONT, world, [
        (Regions.KAKARIKO_VILLAGE, lambda bundle: True),
        (Regions.KAK_POTION_SHOP_BACK, lambda bundle: is_adult(bundle)),
    ])

    # Kak Potion Shop Back
    # Connections
    connect_regions(Regions.KAK_POTION_SHOP_BACK, world, [
        (Regions.KAK_POTION_SHOP_FRONT, lambda bundle: True),
        (Regions.KAK_BACKYARD, lambda bundle: is_adult(bundle)),
    ])

    # Kak Granny's Potion Shop
    # Locations
    add_locations(Regions.KAK_GRANNYS_POTION_SHOP, world, [
        [Locations.KAK_TRADE_ODD_MUSHROOM,
         lambda bundle: is_adult(bundle) and can_use(Items.ODD_MUSHROOM, bundle)],
        (Locations.KAK_GRANNYS_SHOP,
         lambda bundle: is_adult(bundle) and (can_use(Items.ODD_MUSHROOM, bundle)) and trade_quest_step(
             Items.ODD_MUSHROOM, bundle))
    ])
    # Connections
    connect_regions(Regions.KAK_GRANNYS_POTION_SHOP, world, [
        (Regions.KAK_BACKYARD, lambda bundle: True)
    ])

    # Kak Redead Grotto
    # Locations
    add_locations(Regions.KAK_REDEAD_GROTTO, world, [
        (Locations.KAK_REDEAD_GROTTO_CHEST,
         lambda bundle: can_kill_enemy(bundle, enemy=Enemies.REDEAD, combat_range=EnemyDistance.CLOSE,
                                       wall_or_floor=True, quantity=2))
    ])
    # Connections
    connect_regions(Regions.KAK_REDEAD_GROTTO, world, [
        (Regions.KAKARIKO_VILLAGE, lambda bundle: True),
    ])

    # Kak Open Grotto
    # Locations
    add_locations(Regions.KAK_OPEN_GROTTO, world, [
        (Locations.KAK_OPEN_GROTTO_CHEST, lambda bundle: True),
        (Locations.KAK_OPEN_GROTTO_FISH, lambda bundle: has_bottle(bundle)),
        (Locations.KAK_OPEN_GROTTO_GOSSIP_STONE_FAIRY, lambda bundle: call_gossip_fairy(bundle)),
        (Locations.KAK_OPEN_GROTTO_GOSSIP_STONE_BIG_FAIRY, lambda bundle: can_play_song(bundle, Items.SONG_OF_STORMS)),
        (Locations.KAK_OPEN_GROTTO_GOSSIP_STONE, lambda bundle: True),
        (Locations.KAK_OPEN_GROTTO_BEEHIVE_LEFT, lambda bundle: can_break_lower_hives(bundle)),
        (Locations.KAK_OPEN_GROTTO_BEEHIVE_RIGHT, lambda bundle: can_break_lower_hives(bundle)),
        (Locations.KAK_OPEN_GROTTO_GRASS1, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_OPEN_GROTTO_GRASS2, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_OPEN_GROTTO_GRASS3, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.KAK_OPEN_GROTTO_GRASS4, lambda bundle: can_cut_shrubs(bundle)),
    ])
    # Connections
    connect_regions(Regions.KAK_OPEN_GROTTO, world, [
        (Regions.KAK_BACKYARD, lambda bundle: True),
    ])

    # Kak Behind Gate
    # Connections
    connect_regions(Regions.KAK_BEHIND_GATE, world, [
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: is_adult(bundle) or has_item(LocalEvents.KAKARIKO_GATE_OPEN, bundle) or can_do_trick(
             "RT Visible Collision", bundle)),
        (Regions.DEATH_MOUNTAIN, lambda bundle: True)
    ])

    # Kak Well
    # Connections
    connect_regions(Regions.KAK_WELL, world, [
        (Regions.KAKARIKO_VILLAGE,
         lambda bundle: is_adult(bundle) or has_item(Items.BRONZE_SCALE, bundle) or has_item(Events.DRAIN_WELL,
                                                                                             bundle)),
        # TODO: Add check for dungeon entrance randomization
        (Regions.BOTTOM_OF_THE_WELL_ENTRYWAY, lambda bundle: is_child(bundle) or has_item(Events.DRAIN_WELL, bundle)),
    ])
