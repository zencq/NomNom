# ROADMAP

This order could be changed due to new game updates.
Some points need validation to confirm that it's possible thing to do, so some
of them might disappear unimplemented.

### Legend
* [FET] = New features
* [FIX] = Bugfix
* [IMP] = Improvements for existing features
* [INF] = Info or memory aid for me
* [VIS] = Visual enhancement

---

# alpha.17

#### General
* [IMP] Update database to 3.2 + 3.3 + 3.4
* [FET] Transfer save to other platform (#27)
* [FIX] Proper message when selection an invalid path

# beta.1 - Feature Polishing

#### Cross-Save
* [FET] Twitch Rewards, Season Rewards, etc
* [FET] UnlockedTitles
* [FET] UnlockedWikiTopics
* [FET] SeenWikiTopics
* [FET] SeenProducts
* [FET] SeenTechnologies
* [FET] SeenSubstances

#### General
* [IMP] Notification is saving finished
* [IMP] Integration of libMBIN
* [IMP] some UI changes
* [IMP] Handling of customization technology
    * add the "^T_<id>" in KnownTech and "^<id>" in KnownSpecials
    * METADATA/GAMESTATE/PLAYERDATA/BOBBLEHEADCUSTOMISATIONDATA.EXML
    * METADATA/GAMESTATE/PLAYERDATA/THRUSTERCUSTOMISATIONDATA.EXML
* [IMP] Seed mode to set seed as name too (or separate button)
* [IMP] Naming and handling of procedural items
* [IMP] Code cleanup
* [IMP] UI cleanup
* [IMP] new mod mode (useful for modded games)
    * only for Steam as other platforms don't support modding
        * Disables various checks and limitations that can be changed via mods.
        * Unlimited stack size of inventory slots
        * Skip tech overload check
* [IMP] Advanced mode
    * Enables advanced features that can easily destroy a save if you don't
      know what you are doing.
* [IMP] enable multi language support
    * German
    * Korean
* [IMP] overall improvements and more failsafe
* [IMP] create a first crash report before opening the window. update as before in case there is a user comment
* [IMP] hide unimplemented features instead of disabling them
* [IMP] exception always english
* [IMP] switch back to manager-view (or if possible reload current view on-the-fly)
* [IMP] upgrade to .NET 5/6
* [FET] Change gamemode of a save (#12)
* [IMP] Use libMBIN JSON mapping when available (incl download of new ones)

#### Manager
* [VIS] Slot selection: Game Mode icon
* [IMP] Info why an archive is not compatible

#### Editor - Inventory
* [FET] Move between Inventories
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
    * [FET] for proc items downloadable CSV per item with all visible stats
* [FIX] some resources when you add to a ships inventory (or the base inventory) only lets you set 2 for example the gold.. it should be stacking to 500 in the ship
* [FET] Generate Seed for all proc tech

#### Editor - Exosuit
* [IMP] show max health
* [FET] clear space station exosuit interaction
* [VIS] Health/Currency icons

#### Editor - Starship
* [FET] Generate Seed for all
* [FIX] Editor view needs to be reloaded to apply the changed debug mode to the legacy color UI.

#### Editor - Multi-Tool
* [FET] Generate Seed for all
* [FET] Set current weapon mode
* [FET] Legacy Color (3.3+)

#### Editor - Exocraft
* [FIX] Disable+change tab when last one is delete
* [FIX] Disable context menu enable/disable option

#### Editor - Base
* [FET] Delete Base
* [IMP] Disable tab if now base or freighter / storage container to freighter ?
* [FET] Change model of hired NPCSs

#### Editor - Freighter
* [FIX] Directly update UI in Frigates when syncing home seed

#### Editor - Frigates
* [FET] Copy
* [FET] Delete

#### Editor - Discoveries
* [FET] Delete TerrainEdit of any planet
* [FIX] Only rename own base endpoints

#### Editor - Knowledge
* [FIX] Directly update UI in Discovery when changing a word
* [IMP] learned/total and % complete for words for each race (https://github.com/goatfungus/NMSSaveEditor/issues/196)
* [IMP] (un)learn all
* [IMP] improve performance and fix oversized images
* [FIX] "Is Known" checkbox not working
* [FIX] view

#### Editor - Milestones
* [VIS] Add Icons

#### Editor - Companions
* [FET] Evaluate possibilities
* [FET] Unlock slots

#### Catalogue
* [FET] Add Recipe tab
* [IMP] Group DataGrids

---

# beta.2 - Customization

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

#### Editor - Multi-Tool
* [FET] Customization
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

#### Editor - Exocraft
* [FET] Customization

#### Editor - Freighter
* [FET] Customization
* [INF] The Upgrade Station on the freighter bridge can be used to recolour your freighter. Unlock new available colours with nanites. Unlocked colours are permanently available and can be reapplied for free.

#### Editor - Discoveries
* [FET] Unique locations
    * expedition season 1 rendezvous points

#### Editor - Companions
* [FET] Customization

---

# beta.3 - More Editor

#### Editor - Knowledge
* [FET] Unlockable Item Tree (+total of CostType to unlock all)

#### Editor - Mission
* [FET] "^BASE_UPGRADE6" BASE_UPGRADE-Missions have a 1:30h timer.
* [FET] "^BASE_UPGRADE11"-12 (+?) BASE_UPGRADE-Missions have a 6:00h timer.
* [FET] "^???" Living Ship-Missions have a max timer of 24:00h.

---

# beta.4 - Guide

#### Guide
* [FET] Exosuit
    * in-game upgrade cost
* [FET] Starship
    * Inventory when purchase
    * Price (calc by selection, compared to own ships/diff in units to purchase)
    * count per system
* [FET] Farming
    * Grow time
* [FET] Star system
    * Biomes (incl. search for prefix, possible resources) -> METADATA\SIMULATION\SOLARSYSTEM\BIOMES\LUSH\LUSHBIOME.MBIN
    * Is Anomaly in System
    * No of Planets/Moons in System
* [FET] additional stats

---

# beta.5 - Clipboard, Store preferences and manually added stats

#### General
* [FET] Undo/Redo
    * Remember UpDown press/release states and not each increment (same for logging)
* [IMP] Left/Right sidebars collapsible
* [FET] select/display screenshot/image of Starship/multi-tool/(exocraft)/freighter
* [FET] new mode to select if the various states above should be remember across multiple sessions
* [FET] remember various tool states
    * last added item [inventory] -> single session only
    * sidebars collapsed -> single/multi session selectable via mode
    * selected tab -> single session only when switching main sections, setting for default tab (bold name)
    * last loaded platform -> always (move from settings)
    * session count -> always (move from settings)

#### Manager
* [FET] Backup recovery

#### Editor - Inventory
* [FET] Ctrl+C, Ctrl+V to copy inventory slots.

#### Editor - Multi-Tool
* [FET] store Type selection (of seed) -> file

#### Editor - Discoveries
* [FET] Store manual TeleportEndpoint -> file
* [FET] remember ly distance for jumps to center per ship -> file

---

# beta.6 - Import/Export, Raw JSON

#### General
* [FET] Backup/Restore (of Inventory/Starship/Base/Compainions/etc) incl screenshot of NomNom
    * Import Base:
        * New (if not base at this coordinates),
        * append, replace -> base computer as anchor point and will not be replaced
    * Import other:
        * replace
    * https://github.com/charliebanks/nms-base-builder#how-to-use
* [FET] Maybe database downloadable
* [FET] Telemetry?
* [FET] Transfer base to other save

#### JSON Editor
* [FET] Unlock
* [FET] Performant TreeView
* [FIX] Proper return of modified JSON

---

# beta.7 - Finshing

#### General
* [IMP] Code cleanup
* [IMP] UI cleanup

#### Editor - Inventory
* [FIX] Item Details: Min/Max Stats for procedural technology seems switched but has a technical background.
