# ROADMAP

This order could be changed due to new game updates.
Some points need validation to confirm that it's possible thing to do, so some
of them might disappear unimplemented.

### Legend
* [FET] = New feature
* [FIX] = Bugfix
* [IMP] = Improvement for existing feature
* [INF] = Informational or reminder for developer
* [VIS] = Visual enhancement

--------------------------------------------------------------------------------

## beta.next

### General
* [VIS] Complete UI overhaul by switching to the modern Windows design language (Fluent Design)
* [FET] Dark Mode
* [FET] GamePad support
* [IMP] New code editor for JSON
* [IMP] anyedit search for JSON editor
* [IMP] Notification is saving finished/progress bar loaded/saved
* [IMP] Info when new assets are available to download: Pi, Mapping, etc
* [IMP] Toggle checkboxes with space
* [IMP] Cycle through dropdown by key press (eg "A" cycles through galaxies starting with "A")
    * https://discord.com/channels/215514623384748034/215514674869829633/887440399600328756
* [IMP] More details of specific entry in Collection Manager
    * Editable
    * Sort
    * Filter
* [IMP] Show only locked items (Synthesis, etc)
* [FET] "Any Edit" JSON editing via dynamic UI dropdowns (also as search for JSON editor)
* [FIX] Use different database versions
* [FET] determine max stats for weapon, freighter
* [FET] show maneuverability incl min/max stats
* [FET] open details of item in synthesis/catalogue
* [INF] add logs to all actions, not just properties
* [IMP] mode overhaul
    * Debug purely for debugging/programming related stuff
    * restriction modes
        * Vanilla
            * only allow things that a also possible in-game (e.g. non-procedural technology only allowed once per inventory)
        * Default
            * allowing as much as the game allows without forcing something to something else and showing limitations like tech overload
        * Modding (only platforms with modding capability)
            * remove all restrictions and visible hints that can be modded (e.g. don't show tech overload, allowing suit tech inventory to be set to 8x6)
            * Disables various checks and limitations that can be changed via mods.
            * Unlimited stack size of inventory slots
            * Skip tech overload check
            * extensible database
* [IMP] re-check various limitions
    * stats limit
    * freighter hyperdrive is much higher than 1k
* [FET] Undo/Redo
* [IMP] restore ship, etc to empty slots
* [IMP] show files (ending) when selecting a path but take dir anyway

### Catalogue

### Editor - General
* [FET] QuickAction

### Editor - Weapon
* [FET] Legacy Color (3.3+)
* [FET] Set Weapon modes

### Editor - Frigate
* [FET] change all the homes seeds of fleet at once
* [FET] set freighter seeds to current system

### Editor - Catalogue
* [FET] Add Recipe tab
* [FET] Unlockable Item Tree (+total of CostType to unlock all)

### Editor - Mission (Log)
* [FET] new tab `Log` do modify missions
* [FET] "^BASE_UPGRADE6" BASE_UPGRADE-Missions have a 1:30h timer.
* [FET] "^BASE_UPGRADE11"-12 (+?) BASE_UPGRADE-Missions have a 6:00h timer.
* [FET] "^???" Living Ship-Missions have a max timer of 24:00h.

### Editor - Milestones
* [VIS] Add Icons
* [FIX] Directly update UI in Discovery when changing a word
* [FET] show all stats (UI generated like Expedition tab)
    * [INF] generate current stats?

### Editor - Discovery
* [FET] manage/delete discoveries (animals,etc)
* [FET] Show if nexus or freighter are in a system (discoveries)
* distance to other location ?
* add teleport desination for glaxies; https://discord.com/channels/627059745160953866/720411261019619399/1009155586895659109
* [FET] Choose from list of unique (expedition rendezvous, etc)
* [FET] calc hyperdrive range based on tech and Pi (default/min is 101.0 ly) => ship/freighter
* [FET] Delete TerrainEdit of any planet/all
* [IMP] trigger space battle in early game (< 3h/5 warps)
    * set time/warps to 0
    * if time < 3h then set time to 10800
    * if warps < 5 then set warps to 5
* [IMP] filter by galaxy
* [IMP] sort by distance to center, etc
* [FET] show map
    * https://raw.githubusercontent.com/jaszhix/NoMansConnect/master/screenshot.png
    * show path
* [FET] Store current place
    * [VIS] icon: DUI_PLANET.DDS, MISSION.PLANETS.OFF.DDS
*[FET] https://github.com/andraemon/SystemNameCalculator

### Editor - Base
* [FET] NPC Worker Resources/Change model of hired NPCSs
    * [FET] Seed of interactions -> base npc
* [FET] Add cylidrical rooms again
* [FIX] Move base (computer)
* [FET] add/remove SeenBaseBuildingObjects
* [FET] move container/switch position
* [FET] Transfer base to other save
* [FET] plant timer?
* [IMP] detect duplicates (from platform transfer)
* [INF] 400 is max bases you can have
* [FET] Delete Base
* [IMP] Backup/Restore
    * Import Base:
        * New (if not base at this coordinates),
        * append, replace -> base computer as anchor point and will not be replaced
    * Import other:
        * replace
    * https://github.com/charliebanks/nms-base-builder#how-to-use
* [IMP] Load Base Image from Cache

### Editor - ByteBeat
* [VIS] icon: BYTEBEATINTERACTION.DDS, ICON.NOTE.DDS
* [FET] import/export
* [FET] Evaluate possibilities
* [FET] Choose from list of unique (twitch drops, etc)
* https://discord.com/channels/627059745160953866/720411261019619399/966684265234448415

### Editor - Companions
* [FET] Edit last...IncreaseTime
    * https://discord.com/channels/627059745160953866/627110270418026506/948166170589134848
    * Now i've modified "LastTrustIncreaseTime" from 1646123258 to 1046123258. After saving and launching the game, giving the thing 1 gently pat and 1 food treat it automatically reached 100% trust, triggering the milestone

### Editor - Milstones
* [IMP] set progress to done, button (for milestones)

### Editor - Settlement
* [IMP] Class
* [IMP] race based on production
* [IMP] poor/neutral/rich based on production

### Editor - Inventory
* [FIX] ingredient-only restriction to Ingredient Storage container (check current state)
    * not restricted in debug
* [FET] Move between Inventories
    * [FET] copy ship inventories and technologies to other ships
* [FET] integrate inventory backup into collections but also for exosuit
* [VIS] item name in slot move at the same speed and only move in one direction -> https://forums.nexusmods.com/index.php?/topic/8786978-nomnom/page-4#entry85873748
* [IMP] Naming and handling of procedural items
* [FET] Auto-Sort Inventories (#29)
* [FIX] some resources when you add to a ships inventory (or the base inventory) only lets you set 2 for example the gold.. it should be stacking to 500 in the ship
    * <4.0
* [FIX] Min/Max Stats for procedural technology seems switched but has a technical background.
* add repair cost to item details (eg SHIPSLOT_DMG2): https://discord.com/channels/215514623384748034/215514674869829633/928451303053598750
* [IMP] Item Details
    * [FET] for proc items downloadable CSV per item with all visible stats (#24)
        * add versioning to Pi repo for downloading updates
        * get list of class of seed for UP_FRCOM, UP_FREXP, UP_FRFUE, UP_FRHYP, UP_FRMIN, UP_FRSPE, UP_FRTRA
        * search Pi data with weighting
        * built-in top 100 or so but allow doenload of full set nonethelss
        * [FET] button in settings download all assets (proc upgrade CSVs)
        * reverse proc tech names for translation
        * Pi with delta updates
        * [IMP] refiner limits https://discord.com/channels/215514623384748034/215569912121262080/863293366794715136
        * [FIX] proc details messed up https://discord.com/channels/215514623384748034/215514674869829633/919593839050760233
        * use to determine exactly the max health (UP_SHLD1, UP_SHLD2, UP_SHLDX, UP_SNSUIT)
    * [IMP] Creation-Group: Rewards (Consumable, Mission, etc.)
    * [FET] Base Building-Group
    * [FET] Frigate-Group
    * [FET] Learnable-group
    * [IMP] Collapse "Dismantle Return" for maintenance items
    * [IMP] show time to make in refiner list
    * [IMP] personal refiner fuel?
    * [IMP] Product tech module unlock cost in nanites
* [FET] Add resources for building part x times
* [FET] "id"s for tech packages
* [FET] multi-selection for add item/delete/move/etc
* [FET] fill free slots with item (add item window)
* [FET] in add-item-window allow select of no of slots 1 to enabled-empty
* [FET] Ctrl+C, Ctrl+V to copy inventory slots.
* [IMP] open Assistant app dialog for this inventory (collection)

### Customization

#### General
* [INF] Added hover text to all colour, texture and armour style options to the buttons in the customiser, allowing players to know ahead of time what option they are selecting.

#### Exosuit
* [FET] Outfit Customization
    * Outfit
    * Jetpack effect
    * Banner (icon, colors)
    * Titles
    * make capes visible in multi-player
        * https://www.reddit.com/r/NoMansSkyMods/comments/ycnubk/discovery_capes_can_show_in_multiplayer_heres_how/?utm_source=share&utm_medium=android_app&utm_name=androidcss&utm_term=1&utm_content=share_button
#### Starship
* [FET] Color Customization
* [FET] Reset ship color customization

#### Exocraft
* [FET] Customization
* [FET] Reset customization

#### Freighter
* [FET] Customization
* [FET] Reset customization

#### Companions
* [FET] Customization
* [FET] Reset customization
* https://github.com/laanp/NMS-Creature-Builder

--------------------------------------------------------------------------------

--------------------------------------------------------------------------------

# beta.next.next - Guide

#### Guide
* in-game upgrade cost
* [FET] Starship
    * Inventory when purchase
    * Price (calc by selection, compared to own ships/diff in units to purchase)
    * count per system
    * GCSPACESHIPGLOBALS.GLOBAL.MBIN
        *   <Property name="HaulerTakeOffMod" value="1" />
        *   <Property name="FighterTakeOffMod" value="1" />
        *   <Property name="ShuttleTakeOffMod" value="0.66" />
        *   <Property name="ExplorerTakeOffMod" value="0.5" />
        *   <Property name="RoyalTakeOffMod" value="1" />
* [FET] Farming
    * Grow time
* [FET] Star system
    * Biomes (incl. search for prefix, possible resources) -> METADATA\SIMULATION\SOLARSYSTEM\BIOMES\LUSH\LUSHBIOME.MBIN
* [FET] additional stats

--------------------------------------------------------------------------------
