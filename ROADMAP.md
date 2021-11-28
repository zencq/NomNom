# ROADMAP

This order could be changed due to new game updates.
Some points need validation to confirm that it's possible thing to do, so some
of them might disappear unimplemented.

### Legend
* [FET] = New features
* [FIX] = Bugfixes
* [IMP] = Improvements for existing features
* [INF] = Informational or reminder for me
* [VIS] = Visual enhancements

--------------------------------------------------------------------------------

# Settlements & Expeditions

#### Editor - Settlement
* [FET] basic edit feature

#### Editor - Expedition
* [FET] edit expedition progress

--------------------------------------------------------------------------------

# Technical Maintenance

#### General
* [IMP] cli options
    * decompression save/meta
    * import/export json
* [IMP] upgrade to .NET 5/6 (#51)
* [FET] multi-game version-database
    * downloadable
* [IMP] Use libMBIN JSON mapping when available (incl download of new ones) https://discord.com/channels/215514623384748034/215569790801018880/856544044392644608
* [IMP] code cleanup and optimization
* [FIX] not correctly updating UI (at least for ship and bases)
* [IMP] Handling of customization technology
    * add the "^T_<id>" in KnownTech and "^<id>" in KnownSpecials
    * METADATA/GAMESTATE/PLAYERDATA/BOBBLEHEADCUSTOMISATIONDATA.EXML
    * METADATA/GAMESTATE/PLAYERDATA/THRUSTERCUSTOMISATIONDATA.EXML
* [IMP] use https://github.com/nickbabcock/Pfim to display dds image without converting
* [INF] Language Properties
* [INF] add logs to all actions, not just properties
* [FET] store window position and size
* [IMP] hide unimplemented features instead of disabling them
* [IMP] start multi language support again
    * German
    * Korean
* [FET] ~~show supporters in a special window~~ add thanks to about
* [FET] start for help database for all feature
* [IMP] exception always english
* [FIX] Proper message when selection an invalid path/catch excpetion
    * System.UnauthorizedAccessException (Access to the path '...' is denied.)
* [FIX] Check if valid json for single saves
* [FET] new mode to select if the various states above should be remember across multiple sessions
* [FET] remember various tool states
    * last added item [inventory] -> single session only
    * sidebars collapsed -> single/multi session selectable via mode
    * selected tab -> single session only when switching main sections, setting for default tab (bold name)
    * last loaded platform -> always (move from settings)
    * session count -> always (move from settings)
    * windows size and postition
* [IMP] create a first crash report before opening the window. update as before in case there is a user comment
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
* [IMP] Notification is saving finished/progress bar load/save
* [FET] Undo/Redo
    * Remember UpDown press/release states and not each increment (same for logging)
* [IMP] Left/Right sidebars collapsible
* [IMP] re-check various limitions
    * stats limit
    * freighter hyperdrive is much higher than 1k
* [IMP] switch back to manager-view (or if possible reload current view on-the-fly)
* [FET] add settings window to edit things at one place without multiple steps through menus
    * paths
    * modes
    * language
    * landing page
* [FET] add welcome/first-start window
    * supported platforms
    * select platform to start with
        * pre-analysis with what is available
* [FET] remove output path setting and add "open in explorer" menu
    * crash
    * log
    * backup
    * json
    * collection
* [IMP] transform "Save as json" to "import/export json"
* [IMP] cycle through dropdown by key press (eg "A" cycles through galaxies starting with "A")
    * https://discord.com/channels/215514623384748034/215514674869829633/887440399600328756
* [FIX] check path crash. `#` or in NMS install dir or different drive
* [FIX] no meta file = crash
* [FET] wiki window and add to guide
* [IMP] moce links button to left sidebar

#### Manager
* [IMP] pre-analysis with what is available
    * show those as button in path display
* [VIS] Slot selection: Game Mode icon
* [VIS] show GOG icon if "DefaultUser" in save path with valid save
* [IMP] Info why an archive is not compatible
    * show all existing archives, not only valid ones (SaveSlot/Refresh)
* [FET] Backup recovery
    * backup files for meta and data
    * additional list for backups of slot and platform
    * button for additional list to load data in backup to current archive
    * button to restore backup to any archive (like move)
* [IMP] platform transfer (#61)
    * add default steam/ms selection to platform transfer (see pre-analysis)
    * add selection which bases you want to keep (to avoid duplication/conflicts with uploaded bases)
        * https://discord.com/channels/627059745160953866/720411261019619399/905098763171946586
    * check for same location in both save paths
    * check overwriting existing slots not working
    * show both platform icons in area
    * show done confirmation with asking for reloading of target platform
    * show used slots on target
    * update bytebeat, settlement, companion
    * step by step wizard (maybe also other places)
* [IMP] add catch for failing platforms: https://discord.com/channels/762409407488720918/767096981897347075/883122385367232522

#### Cross-Save
* [IMP] extract username from saves and use to display in account title unlock
* [IMP] unlock all/each season via button

#### Editor - General
* [IMP] restore/delete mission (un)related to the new game mode

#### Editor - Inventory
* [IMP] add remaining images
* [FIX] Min/Max Stats for procedural technology seems switched but has a technical background.
* [FIX] re-check "enter" to execute search.
* [FIX] Fill all chargeable slots isn't working for starships and exocraft.
* [FIX] Ctrl+E is not working for starships, exocraft (Ctrl-F works fine)
* [FIX] Add/replace item has greyed out after a while. Possibly after I expanded storage container capacities

#### Editor - Knowledge/Synthesis Bot
* [FIX] Directly update UI in Discovery when changing a word
* [IMP] learned/total and % complete for words for each race (https://github.com/goatfungus/NMSSaveEditor/issues/196)
* [IMP] (un)learn all
* [IMP] add search
* [IMP] unlock rewards for each season/twich drop

--------------------------------------------------------------------------------

# Collections

#### General
* [FET] select/display screenshot/image of Starship/multi-tool/(exocraft)/freighter
* [FET] Backup/Restore (of Inventory/Starship/Base/Compainions/etc) incl screenshot of NomNom
    * Import Base:
        * New (if not base at this coordinates),
        * append, replace -> base computer as anchor point and will not be replaced
    * Import other:
        * replace
    * https://github.com/charliebanks/nms-base-builder#how-to-use
* [FET] NMSC feature set
* [FET] Links to seed central Discord etc
* [FET] store ship and pet seeds in a favourite list

#### Editor - Starship
* [FET] Choose from list of unique seeds (Pre-order/starter/expedition/twitch drops, https://discord.com/channels/627059745160953866/627143858094080030/820073927295762492)
    * Alpha Vector, PS4 Preorder bonus ship (ALPHAVSHIP): 0x8E8E2193DD4A9EDA
    * Horizon Omega, PC Preorder bonus ship (HORIZOSHIP): 0xC4C9C1AABCA59FE6
    * Rasamama S36, original starter ship (1.0~1.2): 0x867BFFC553B294A8
    * Yakomaku S79, Atlas Rises starter ship (1.3): 0xA547AB958C97E439
    * Radiant Pillar BC1, current version / NEXT starter ship (1.5 ~ Current): 0xA547AB958C97E439
    * ---
    * Honmatan OQ5 (Explorer), Reward from Expedition Season 1 Phase 4 mission The Good ship, Acquire an A-class starship: 0x867BFFC553B294A8
    * ---
    * Hadach's Discovery KH3 (Fighter), Reward from Expedition Season 2 Phase 2 Completion: 0x94B00527B67F46EF
    * ---
    * Eokai's Prime Inquirer, Day1 Twitch Drops (Explorer): 0xF437579A7A76D819
    * Hoshis HP7, Day2 Twitch Drops (Fighter): 0x6FF7793FBC58837
    * Nemesis of the Kudama, Day3 Twitch Drops (Fighter): 0xBCEF59E1A64E28DC
    * Ultimate Pride JB2, Day4 Twitch Drops (Hauler): 0x9557186C7D37C2EC
    * Prime Song JZ4, Day5 Twitch Drops (Shuttle): 0x9E58062EEDC436B
    * ---
    * Hiwamiha of Destiny (Fighter), Day- Twitch Drops: 0x19036EFEDEA6E86D
    * VV5 Ariyaz (Shuttle), Day- Twitch Drops: 0xEACE5BEA27F0A3CC
    * Jirishi's Prospect (Explorer), Day- Twitch Drops: 0xAB8668AAA38F66CF
    * Hadach's Discovery KH3 (Fighter), Day- Twitch Drops: 0x94B00527B67F46EF
    * Ultimate Sleep LO1 (Hauler), Day- Twitch Drops: 0x3A8B8466974433AA


#### Editor - Multi-Tool
* [FET] Choose from list of unique seeds (Pre-order/starter/expedition/twitch drops, https://discord.com/channels/627059745160953866/627143858094080030/820073927295762492)
    * Experiment C6/4 / Waveform Focuser N56-P (Multitool), Starter MT: 0x55907B79D95B675B
    * Rezosu Z65 (REZOSUZ65), PS4 preorder bonus MT: 0xCDDB99E6DCE0749C
    * Artios-VI (ENT_XOGUN1), Xbox preorder bonus MT:  0x5BA94DDC4D81618C
    * Vertic-LX (ENT_XOGUN2), Microsoft store digital preorder bonus MT - 0xDEB7E483C1A3F7F8
    * ---
    * Surge of Storms B56-K1-6 (Experimental Compact Pistol), Reward from Expedition Season 1 Phase 2 Completion: 0xCF9858143BDCE787
    * Geometric Dream Inverter (Alien Pistol), Reward from Expedition Season 1 Phase 5 mission Boundary Failure, Eliminate 50 sentinels: 0xE0AF6FA5D33EE25D
    * ---
    * Quantum Harmoniser Mark IV, Day1 Twitch Drops Rifle MT: 0x7E9896D06EF5510A
    * Loop Scoop Mark IV, Day2 Twitch Drops Pistol MT: 0x33156C44DD934D25
    * Arc Capacitor W/17I-15P, Day3 Twitch Drops Pistol MT: 0x8F2D0700120E1149
    * Hunevar's Dream Charger, Day4 Twitch Drops Experimental Compact Pistol MT: 0xFB8D9BA3FC5021F
    * Imperfect Loop Reflector, Day5 Twitch Drops Rifle MT: 0x73DD2FD7DE1FFD45
* [FET] store Type selection (of seed) -> file


#### Editor - Companions
* [FET] Choose from list of unique pets (twitch drops, etc)

#### Editor - Base
* [FET] Seed of interactions -> base npc
* [FET] import/export

#### Editor - Discoveries
* [FET] Unique locations
    * expedition rendezvous points
* [FET] Store manual TeleportEndpoint -> file
* [FET] remember ly distance for jumps to center per ship -> file

#### Editor - PLANETARY SETTLEMENTS
* [FET] Evaluate possibilities
    * https://discord.com/channels/627059745160953866/720411261019619399/883365755914182687
* [FET] add new tab to modify your SETTLEMENTS

--------------------------------------------------------------------------------

# Feature Polishing

#### General
* [IMP] separate button to set seed as name too

#### Editor - Inventory
* [FET] Move between Inventories
* [FET] copy ship inventories and technologies to other ships
* [FET] integrate inventory backup into collections but also for exosuit
* [FIX] ingredient-only restriction to Ingredient Storage container (check current state)
    * not restricted in debug
* [FET] change product multiplier
* [IMP] cache last added item
* [VIS] item name in slot move at the same speed and only move in one direction -> https://forums.nexusmods.com/index.php?/topic/8786978-nomnom/page-4#entry85873748
* Item Details
    * [IMP] Creation-Group: Rewards (Consumable, Mission, etc.)
    * [FET] Base Building-Group
    * [IMP] Collapse "Dismantle Return" for maintenance items
    * [IMP] show time to make in refiner list
    * [FET] Frigate-Group
    * [FET] Learnable-group
    * [IMP] personal refiner fuel?
    * [IMP] Product tech module unlock cost in nanites
    * [FET] for proc items downloadable CSV per item with all visible stats (#24)
        * add versioning to Pi repo for downloading updates
        * get list of class of seed for UP_FRCOM, UP_FREXP, UP_FRFUE, UP_FRHYP, UP_FRMIN, UP_FRSPE, UP_FRTRA
        * search Pi data with weighting
    * [IMP] refiner limits https://discord.com/channels/215514623384748034/215569912121262080/863293366794715136
* [FIX] some resources when you add to a ships inventory (or the base inventory) only lets you set 2 for example the gold.. it should be stacking to 500 in the ship
* [IMP] Naming and handling of procedural items
* [FET] Ctrl+C, Ctrl+V to copy inventory slots.
    * [FET] right click drag-drop to duplicate slot
    * [FET] multi-selection for add item/delete/move/etc
* [FET] Auto-Sort Inventories (#29)
* [FET] Add resources for building part x times

#### Editor - Exosuit
* [IMP] show max health
* [FET] clear space station exosuit interaction
* [VIS] Health/Currency icons

#### Editor - Starship
* [FET] Generate Seed for all
* [FIX] Editor view needs to be reloaded to apply the changed debug mode to the legacy color UI.
* [FET] copy inventory to other ship
* [FET] re-order

#### Editor - Multi-Tool
* [FET] Generate Seed for all
* [FET] Set current weapon mode
* [FET] Legacy Color (3.3+)
* [FET] re-order

#### Editor - Exocraft
* [FIX] Disable+change tab when last one is delete
* [FIX] Disable context menu enable/disable option

#### Editor - Companions
* [FET] Evaluate possibilities
* [FET] re-order
* [FET] Is it possible to pull discovered creature seeds from your save without adopting said creature first? https://discord.com/channels/627059745160953866/720411261019619399/853772131736748053

#### Editor - Base
* [FET] Delete Base
    * detect duplicates (from platform transfer)
* [IMP] Disable tab if now base or freighter / storage container to freighter ?
* [FET] Change model of hired NPCSs
* [FET] Transfer base to other save
* [FIX] hide "clear terrain" when freighter is selected
* [FIX] update base view to update UI when chaning the base selection
* [FIX] move base comuputer selection is empty
* [FET] Add single base objects to list of teleport destination
* [FET] show "featured", "reported" flags
* [IMP] Base part count information display (#56)
* [FET] move container/switch position
* [INF] 400 is max bases you can have
* [FET] re-order
* [FET] add/remove SeenBaseBuildingObjects

#### Editor - Settlement
* [FET] Evaluate possibilities
* [FET] re-order

#### Editor - Freighter
* [FIX] Directly update UI in Frigates when syncing home seed
* [FET] set freighter seeds to current system

#### Editor - Frigates
* [FET] Copy
* [FET] Delete
* [FET] tooltips for stats
* [FET] max out expeditions
* [FET] re-order

#### Editor - Discoveries
* [FET] Delete TerrainEdit of any planet/all
* [FIX] Only rename own base endpoints
* [FET] manage/delete discoveries (animals,etc)
* [FET] Show if nexus or freighter are in a system (discoveries)

#### Editor - Milestones
* [VIS] Add Icons

#### Catalogue
* [FET] Add Recipe tab
* [IMP] Group DataGrids

--------------------------------------------------------------------------------

# Missions

#### Editor - Expeditions
* [FET] new tab do modify the expeditions progress https://www.reddit.com/r/NoMansSkyMods/comments/mp8qi3/how_to_get_golden_vector_plus_other_rewards_save/gv0jibr/

#### Editor - Mission
* [FET] new tab do modify missions
* [FET] "^BASE_UPGRADE6" BASE_UPGRADE-Missions have a 1:30h timer.
* [FET] "^BASE_UPGRADE11"-12 (+?) BASE_UPGRADE-Missions have a 6:00h timer.
* [FET] "^???" Living Ship-Missions have a max timer of 24:00h.
* [FET] show Community Mission progress (https://api.nmsassistant.com/index.html)
    * GET "​/HelloGames​/CommunityMission" Get Latest Community Mission.

--------------------------------------------------------------------------------

# Customization

#### General
* [INF] Added hover text to all colour, texture and armour style options to the buttons in the customiser, allowing players to know ahead of time what option they are selecting.

#### Editor - Exosuit
* [FET] Customization
* Added the ability to add a custom Title to your player name.
    * Titles can be selected at the Customiser.
    * Titles are earned for a large variety in in-game achievements.
    * The unlocked titles are listed in [NMS_installation_Path]\Binaries\SETTINGS\GCUSERSETTINGSDATA.MXML
    * You can grab the title IDs from METADATA\GAMESTATE\PLAYERDATA\PLAYERTITLEDATA.MBIN and add them to the settings file.

#### Editor - Starship
* [FET] Customization (https://github.com/goatfungus/NMSSaveEditor/issues/231, https://www.reddit.com/r/NoMansSkyMods/comments/dkob5c/manual_ship_and_multitool_color_customization/)
    * https://nmscd.github.io/nmscolorparser/
* [FET] Custom Ship (https://discord.com/channels/627059745160953866/687350943859212312/687362600333345026)
* [FET] reset ship color customization

#### Editor - Multi-Tool
* [FET] Customization
* [FET] reset MT color customization

#### Editor - Exocraft
* [FET] Customization
* [FET] reset vehicle customization

#### Editor - Freighter
* [FET] Customization
* [INF] The Upgrade Station on the freighter bridge can be used to recolour your freighter. Unlock new available colours with nanites. Unlocked colours are permanently available and can be reapplied for free.
* [FET] reset freighter color customization

#### Editor - Companions
* [FET] Customization
* [FET] reset Companions customization

--------------------------------------------------------------------------------

# Guide

#### Guide
* [FET] Exosuit
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
    * Is Anomaly in System
    * No of Planets/Moons in System
* [FET] additional stats

--------------------------------------------------------------------------------

# Finish Line

#### Editor - Knowledge
* [FET] Unlockable Item Tree (+total of CostType to unlock all)

#### JSON Editor
* [FET] Performant TreeView

--------------------------------------------------------------------------------
