from typing import TYPE_CHECKING

from ...Enums import *
from ...LogicHelpers import *

if TYPE_CHECKING:
    from worlds.oot_soh import SohWorld

class EventLocations(str, Enum):
    DMC_GOSSIP_STONE_FAIRY = "Death Mountain Crater Gossip Stone Fairy"
    DMC_BEAN_PLANT_FAIRY = "Death Mountain Crater Bean Plant Fairy"


def set_region_rules(world: "SohWorld") -> None:
    player = world.player
    
    ## Death Mountain Crater Upper Nearby
    # Connections
    connect_regions(Regions.DMC_UPPER_NEARBY, world, [
        (Regions.DMC_UPPER_LOCAL, lambda bundle: fire_timer(bundle) >= 48),
        (Regions.DEATH_MOUNTAIN_SUMMIT, lambda bundle: True),
        (Regions.DMC_UPPER_GROTTO, lambda bundle: blast_or_smash(bundle) and (fire_timer(bundle) >= 8 or hearts(bundle) >= 3)),
    ])

    ## Death Mountain Crater Upper Local
    # Events
    add_events(Regions.DMC_UPPER_LOCAL, world, [
        (EventLocations.DMC_GOSSIP_STONE_FAIRY, Events.CAN_ACCESS_FAIRIES, lambda bundle: has_explosives(bundle) and call_gossip_fairy_except_suns(bundle) and (fire_timer(bundle) >= 16 or hearts(bundle) >= 3))
    ])
    # Locations
    add_locations(Regions.DMC_UPPER_LOCAL, world, [
        (Locations.DMC_WALL_FREESTANDING_PO_H, lambda bundle: fire_timer(bundle) >= 16 or hearts(bundle) >= 3),
        (Locations.DMC_GS_CRATE, lambda bundle: (fire_timer(bundle) >= 8 or hearts(bundle) >= 3) and is_child(bundle) and can_attack(bundle) and can_break_crates(bundle)),
        (Locations.DMC_GOSSIP_STONE_FAIRY, lambda bundle: call_gossip_fairy_except_suns(bundle) and has_explosives(bundle) and (fire_timer(bundle) >= 16 or hearts(bundle) >= 3)),
        (Locations.DMC_GOSSIP_STONE_BIG_FAIRY, lambda bundle: can_use(Items.SONG_OF_STORMS, bundle) and (fire_timer(bundle) >= 16 or hearts(bundle) >= 3)),
        (Locations.DMC_CRATE, lambda bundle: (fire_timer(bundle) >= 8 or hearts(bundle) >= 3) and is_child(bundle) and can_break_crates(bundle))
    ])
    # Connections
    connect_regions(Regions.DMC_UPPER_LOCAL, world, [
        (Regions.DMC_UPPER_NEARBY, lambda bundle: True),
        (Regions.DMC_LADDER_REGION_NEARBY, lambda bundle: fire_timer(bundle) >= 16 or hearts(bundle) >= 3),
        (Regions.DMC_CENTRAL_NEARBY, lambda bundle: is_adult(bundle) and can_use(Items.GORON_TUNIC, bundle) and can_use(Items.DISTANT_SCARECROW, bundle) and (effective_health(bundle) > 2 or (can_use(Items.BOTTLE_WITH_FAIRY, bundle) and False or can_use(Items.NAYRUS_LOVE, bundle)))), # TODO Implement Dungeon Shuffle Option to replace False
        (Regions.DMC_LOWER_NEARBY, lambda bundle: False),
        (Regions.DMC_DISTANT_PLATFORM, lambda bundle: (fire_timer(bundle) >= 48 or hearts(bundle) >= 2) or hearts(bundle) >= 3),
    ])

    ## Death Mountain Crater Ladder Area Nearby
    # Locations
    add_locations(Regions.DMC_LADDER_REGION_NEARBY, world, [
        (Locations.DMC_DEKU_SCRUB, lambda bundle: is_child(bundle) and can_stun_deku(bundle))
    ])
    # Connections
    connect_regions(Regions.DMC_LADDER_REGION_NEARBY, world, [
        (Regions.DMC_UPPER_NEARBY, lambda bundle: hearts(bundle) >= 3),
        (Regions.DMC_LOWER_NEARBY, lambda bundle: hearts(bundle) >= 3 and (can_use(Items.HOVER_BOOTS, bundle) or (can_do_trick(Tricks.DMC_BOULDER_JS, bundle) and is_adult(bundle) and can_use(Items.MEGATON_HAMMER, bundle)) or (can_do_trick("DMC Boulder Skip", bundle) and is_adult(bundle))))
    ])

    ## Death Mountain Crater Lower Nearby
    # Locations
    add_locations(Regions.DMC_LOWER_NEARBY, world, [
        (Locations.DMC_NEAR_GCPOT1, lambda bundle: can_break_pots(bundle)),
        (Locations.DMC_NEAR_GCPOT2, lambda bundle: can_break_pots(bundle)),
        (Locations.DMC_NEAR_GCPOT3, lambda bundle: can_break_pots(bundle)),
        (Locations.DMC_NEAR_GCPOT4, lambda bundle: can_break_pots(bundle))
    ])
    # Connections
    connect_regions(Regions.DMC_LOWER_NEARBY, world, [
        (Regions.DMC_LOWER_LOCAL, lambda bundle: fire_timer(bundle) >= 48),
        (Regions.GC_DARUNIAS_CHAMBER, lambda bundle: True),
        (Regions.DMC_GREAT_FAIRY_FOUNTAIN, lambda bundle: can_use(Items.MEGATON_HAMMER, bundle)),
        (Regions.DMC_HAMMER_GROTTO, lambda bundle: is_adult(bundle) and can_use(Items.MEGATON_HAMMER, bundle))
    ])

    ## Death Mountain Crater Lower Local
    # Connections
    connect_regions(Regions.DMC_LOWER_LOCAL, world, [
        (Regions.DMC_LOWER_NEARBY, lambda bundle: True),
        (Regions.DMC_LADDER_REGION_NEARBY, lambda bundle: fire_timer(bundle) >= 8 or hearts(bundle) >= 3),
        (Regions.DMC_CENTRAL_NEARBY, lambda bundle: (can_use(Items.HOVER_BOOTS, bundle) or can_use(Items.HOOKSHOT, bundle)) and (fire_timer(bundle) >= 8 or hearts(bundle) >= 3)),
        (Regions.DMC_CENTRAL_LOCAL, lambda bundle: (can_use(Items.HOVER_BOOTS, bundle) or can_use(Items.HOOKSHOT, bundle) or (is_adult(bundle) and can_shield(bundle) and can_do_trick(Tricks.DMC_BOLERO_JUMP, bundle))) and fire_timer(bundle) >= 24)
    ])

    ## Death Mountain Crater Volcano Vent
    ### This is a deviation from the original SOH logic because of the uni
    add_locations(Regions.DMC_VOLCANO_VENT, world, [
        (Locations.DMC_VOLCANO_FREESTANDING_PO_H, lambda bundle: True),
    ])
    # Connections
    connect_regions(Regions.DMC_VOLCANO_VENT, world, [
        (Regions.DMC_CENTRAL_NEARBY, lambda bundle: True)
    ])

    ## Death Mountain Crater Central Nearby
    # Locations
    add_locations(Regions.DMC_CENTRAL_NEARBY, world, [
        (Locations.SHEIK_IN_CRATER, lambda bundle: is_adult(bundle) and (fire_timer(bundle) >= 8 or hearts(bundle) >= 3))
    ])
    # Connections
    connect_regions(Regions.DMC_CENTRAL_NEARBY, world, [
        (Regions.DMC_CENTRAL_LOCAL, lambda bundle: fire_timer(bundle) >= 48),
        (Regions.DMC_VOLCANO_VENT, lambda bundle: is_adult(bundle) and hearts(bundle) >= 3 and can_do_trick(Tricks.DMC_HOVER_BEAN_POH, bundle) and can_use(Items.HOVER_BOOTS, bundle)),

    ])

    ## Death Mountain Crater Central Local
    # Events
    add_events(Regions.DMC_CENTRAL_LOCAL, world, [
        (EventLocations.DMC_BEAN_PLANT_FAIRY, Events.CAN_ACCESS_FAIRIES, lambda bundle: can_use(Items.MAGIC_BEAN, bundle) and can_use(Items.SONG_OF_STORMS, bundle) and (fire_timer(bundle) >= 8 or hearts(bundle) >= 3))
    ])
    # Locations
    add_locations(Regions.DMC_CENTRAL_LOCAL, world, [
        (Locations.DMC_GS_BEAN_PATCH, lambda bundle: (fire_timer(bundle) >= 8 or hearts(bundle) >= 3) and can_spawn_soil_skull(bundle) and can_attack(bundle)),
        (Locations.DMC_NEAR_WARP_PLATFORM_RED_RUPEE, lambda bundle: is_child(bundle)),
        (Locations.DMC_MIDDLE_PLATFORM_RED_RUPEE, lambda bundle: is_child(bundle) and (fire_timer(bundle) >= 8 or hearts(bundle) >= 3)),
        (Locations.DMC_MIDDLE_PLATFORM_BLUE_RUPEE1, lambda bundle: is_child(bundle) and (fire_timer(bundle) >= 8 or hearts(bundle) >= 3)),
        (Locations.DMC_MIDDLE_PLATFORM_BLUE_RUPEE2, lambda bundle: is_child(bundle) and (fire_timer(bundle) >= 8 or hearts(bundle) >= 3)),
        (Locations.DMC_MIDDLE_PLATFORM_BLUE_RUPEE3, lambda bundle: is_child(bundle) and (fire_timer(bundle) >= 8 or hearts(bundle) >= 3)),
        (Locations.DMC_MIDDLE_PLATFORM_BLUE_RUPEE4, lambda bundle: is_child(bundle) and (fire_timer(bundle) >= 8 or hearts(bundle) >= 3)),
        (Locations.DMC_MIDDLE_PLATFORM_BLUE_RUPEE5, lambda bundle: is_child(bundle) and (fire_timer(bundle) >= 8 or hearts(bundle) >= 3)),
        (Locations.DMC_MIDDLE_PLATFORM_BLUE_RUPEE6, lambda bundle: is_child(bundle) and (fire_timer(bundle) >= 8 or hearts(bundle) >= 3)),
        (Locations.DMC_BEAN_SPROUT_FAIRY1, lambda bundle: is_child(bundle) and can_use(Items.MAGIC_BEAN, bundle) and can_use(Items.SONG_OF_STORMS, bundle) and (fire_timer(bundle) >= 8 or hearts(bundle) >= 3)),
        (Locations.DMC_BEAN_SPROUT_FAIRY2, lambda bundle: is_child(bundle) and can_use(Items.MAGIC_BEAN, bundle) and can_use(Items.SONG_OF_STORMS, bundle) and (fire_timer(bundle) >= 8 or hearts(bundle) >= 3)),
        (Locations.DMC_BEAN_SPROUT_FAIRY3, lambda bundle: is_child(bundle) and can_use(Items.MAGIC_BEAN, bundle) and can_use(Items.SONG_OF_STORMS, bundle) and (fire_timer(bundle) >= 8 or hearts(bundle) >= 3))
    ])
    # Connections
    connect_regions(Regions.DMC_CENTRAL_LOCAL, world, [
        (Regions.DMC_CENTRAL_NEARBY, lambda bundle: True),
        (Regions.DMC_LOWER_NEARBY, lambda bundle: (is_adult(bundle) and can_plant_bean(bundle)) or can_use(Items.HOVER_BOOTS, bundle) or can_use(Items.HOOKSHOT, bundle)),
        (Regions.DMC_UPPER_NEARBY, lambda bundle: is_adult(bundle) and can_plant_bean(bundle)) 
        (Regions.FIRE_TEMPLE_ENTRYWAY, lambda bundle: (is_child(bundle) and hearts(bundle) >= 3 and False) or (is_adult(bundle) and fire_timer(bundle) >= 24)), # TODO Implement Dungeon Shuffle Option to replace False
        (Regions.DMC_DISTANT_PLATFORM, lambda bundle: (fire_timer(bundle) >= 48 or hearts(bundle) >= 2) and can_use(Items.DISTANT_SCARECROW, bundle)),
        (Regions.DMC_VOLCANO_VENT, lambda bundle: is_adult(bundle) and hearts(bundle) >= 3 and can_plant_bean(bundle))
    ])

    ## Death Mountain Crater Great Fairy Fountain
    # Locations
    add_locations(Regions.DMC_GREAT_FAIRY_FOUNTAIN, world, [
        (Locations.DMC_GREAT_FAIRY_REWARD, lambda bundle: can_use(Items.ZELDAS_LULLABY, bundle))
    ])
    # Connections
    connect_regions(Regions.DMC_GREAT_FAIRY_FOUNTAIN, world, [
        (Regions.DMC_LOWER_LOCAL, lambda bundle: True)
    ])

    ## Death Mountain Crater Upper Grotto
    # Locations
    add_locations(Regions.DMC_UPPER_GROTTO, world, [
        (Locations.DMC_UPPER_GROTTO_CHEST, lambda bundle: True),
        (Locations.DMC_UPPER_GROTTO_FISH, lambda bundle: has_bottle(bundle)),
        (Locations.DMC_UPPER_GROTTO_GOSSIP_STONE_FAIRY, lambda bundle: call_gossip_fairy(bundle)),
        (Locations.DMC_UPPER_GROTTO_GOSSIP_STONE_BIG_FAIRY, lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.DMC_UPPER_GROTTO_BEEHIVE_LEFT, lambda bundle: can_break_lower_hives(bundle)),
        (Locations.DMC_UPPER_GROTTO_BEEHIVE_RIGHT, lambda bundle: can_break_lower_hives(bundle)),
        (Locations.DMC_UPPER_GROTTO_GRASS1, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DMC_UPPER_GROTTO_GRASS2, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DMC_UPPER_GROTTO_GRASS3, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.DMC_UPPER_GROTTO_GRASS4, lambda bundle: can_cut_shrubs(bundle))
    ])
    # Connections
    connect_regions(Regions.DMC_UPPER_GROTTO, world, [
        (Regions.DMC_UPPER_LOCAL, lambda bundle: True)
    ])

    ## Death Mountain Crater Hammer Grotto
    # Locations
    add_locations(Regions.DMC_HAMMER_GROTTO, world, [
        (Locations.DMC_DEKU_SCRUB_GROTTO_LEFT, lambda bundle: can_stun_deku(bundle)),
        (Locations.DMC_DEKU_SCRUB_GROTTO_RIGHT, lambda bundle: can_stun_deku(bundle)),
        (Locations.DMC_DEKU_SCRUB_GROTTO_CENTER, lambda bundle: can_stun_deku(bundle)),
        (Locations.DMC_HAMMER_GROTTO_BEEHIVE, lambda bundle: can_break_upper_beehives(bundle))
    ])
    # Connections
    connect_regions(Regions.DMC_HAMMER_GROTTO, world, [
        (Regions.DMC_LOWER_LOCAL, lambda bundle: True)
    ])

    ## Death Mountain Crater Distant Platform
    # Locations
    add_locations(Regions.DMC_DISTANT_PLATFORM, world, [
        (Locations.DMC_DISTANT_PLATFORM_RUPEE1, lambda bundle: is_adult(bundle)),
        (Locations.DMC_DISTANT_PLATFORM_RUPEE2, lambda bundle: is_adult(bundle)),
        (Locations.DMC_DISTANT_PLATFORM_RUPEE3, lambda bundle: is_adult(bundle)),
        (Locations.DMC_DISTANT_PLATFORM_RUPEE4, lambda bundle: is_adult(bundle))
        (Locations.DMC_DISTANT_PLATFORM_RUPEE5, lambda bundle: is_adult(bundle)),
        (Locations.DMC_DISTANT_PLATFORM_RUPEE6, lambda bundle: is_adult(bundle)),
        (Locations.DMC_DISTANT_PLATFORM_RED_RUPEE, lambda bundle: is_adult(bundle))
    ])
    # Connections
    connect_regions(Regions.DMC_DISTANT_PLATFORM, world, [
        (Regions.DMC_CENTRAL_LOCAL, lambda bundle: fire_timer(bundle) >= 48 and can_use(Items.DISTANT_SCARECROW, bundle))
    ])