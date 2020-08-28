# ROADMAP

This order could be changed due to new game updates.

### Legend
* [FET] = New features
* [FIX] = Bugfix
* [IMP] = Improvements for existing features
* [INF] = Info or memory aid for me
* [VIS] = Visual enhancement

---

# alpha.7 - Desolation Update

* [INF] The ability to use the derelict freighter’s engineering system to extract a piece of the freighter’s technology to fit into your own capital ship.
* [INF] The ability to use the derelict freighter’s engineering system to generate new inventory slots for your capital ship. Take new expandable bulkheads to the Upgrade Station on your freighter bridge to apply them.
* [INF] Storage Containers built upon a freighter base now add tabs to the freighter’s inventory page, allowing quick management of freighter inventory contents.
* [INF] Fixed an issue that prevented the installation of technology within a freighter’s general inventory.
* [INF] Improved the display and clarity of the stats displayed on the freighter inventory screen.

* [INF] Capital ships now contribute stats to the success of fleet expeditions. Different freighters have different base levels of Fleet Coordination. This stat can be improved with new procedural technologies salvaged from derelict or abandoned freighters.
* [INF] The expedition UI now shows the difference between stats contributed by the fleet and stats contributed by temporary frigate upgrades or any capital ship technologies.

* [INF] In general, player weapon reload speeds have been reduced and clip sizes increased.
* [INF] The base damage of the Boltcaster has been increased.
* [INF] Ricochet is no longer in the pool of procedural upgrades. Specific technologies have been added to the research tree on the Space Anomaly that will add ricochet functionality to weapons if desired.

* [IMP] Added support for the Microsoft/Windows Store version

---

# alpha.8 - Customization

* [INF] Added hover text to all colour, texture and armour style options to the buttons in the customiser, allowing players to know ahead of time what option they are selecting.

#### Editor - Exosuit
* [FET] Customization
* Added the ability to add a custom Title to your player name.
    * Titles can be selected at the Customiser.
    * Titles are earned for a large variety in in-game achievements.

#### Editor - Starship
* [FET] Customization (https://github.com/goatfungus/NMSSaveEditor/issues/231)

#### Editor - Multi-Tool
* [FET] Customization

#### Editor - Exocraft
* [FET] Customization

#### Editor - Freighter
* [FET] Customization
* [INF] The Upgrade Station on the freighter bridge can be used to recolour your freighter. Unlock new available colours with nanites. Unlocked colours are permanently available and can be reapplied for free.

---

# alpha.9 - Editor Feature Polishing

#### General
* [IMP] Integration of libMBINex
* [IMP] some UI changes
* [IMP] Handling of customization technology
    * add the "^T_<id>" in KnownTech and "^<id>" in KnownSpecials
    * METADATA/GAMESTATE/PLAYERDATA/BOBBLEHEADCUSTOMISATIONDATA.EXML
    * METADATA/GAMESTATE/PLAYERDATA/THRUSTERCUSTOMISATIONDATA.EXML
* [IMP] Seed mode to set seed as name too (or separate button)

#### Editor - Inventory
* [FET] Move between Inventories
* [FIX] ingredient-only restriction to Ingredient Storage container (check current state)
    * not restricted in debug
* [FET] change product multiplier
* Item Details
    * [IMP] Creation-Group: Rewards (Consumable, Mission, etc.)
    * [FET] Base Building-Group
    * [IMP] Collapse "Dismantle Return" for maintenance items
    * [IMP] show time to make in refiner list
    * [FET] Frigate-Group
    * [FET] Learnable-group

#### Editor - Exosuit
* [IMP] show max health

#### Editor - Starship
* [FET] Generate Seed for all

#### Editor - Multi-Tool
* [FET] Generate Seed for all
* [FET] Set current weapon mode

#### Editor - Base
* [FET] Delete Base
* [IMP] Disable tab if now base or freighter / storage container to freighter ?
* [FET] Change model of hired NPCSs

#### Editor - Frigates
* [FET] Copy
* [FET] Delete

#### Editor - Discoveries
* [FET] Delete TerrainEdit of any planet

#### Editor - Knowledge
* [IMP] learned/total and % complete for words for each race (https://github.com/goatfungus/NMSSaveEditor/issues/196)
* [IMP] (un)learn all
* [IMP] improve performance and fix oversized images
* [FIX] "Is Known" checkbox not working

---

# alpha.10 - More Editor

#### Editor - Knowledge
* [FET] Unlockable Item Tree (+total of CostType to unlock all)

#### Editor - Mission
* [FET] "^BASE_UPGRADE6" BASE_UPGRADE-Missions have a 1:30h timer.
* [FET] "^BASE_UPGRADE11"-12 (+?) BASE_UPGRADE-Missions have a 6:00h timer.
* [FET] "^???" Living Ship-Missions have a max timer of 24:00h.

---

# alpha.11 - Catalogue Polishing

#### Catalogue
* [FET] Add Recipe tab
* [IMP] Group DataGrids

---

# alpha.12 - Guide

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

# alpha.13 - Clipboard, Store preferences and manually added stats

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

# alpha.14 - Import/Export, Raw JSON

#### General
* [FET] Backup/Restore (of Inventory/Starship/Base/etc) incl screenshot of NomNom
    * Import Base:
        * New (if not base at this coordinates),
        * append, replace -> base computer as anchor point and will not be replaced
    * Import other:
        * replace
* [FET] Maybe database downloadable
* [FET] Telemetry?
* [FET] Transfer base to other save
* [FET] Transfer save to other platform

#### JSON Editor
* [FET] Unlock
* [FET] Performant TreeView
* [FIX] Proper return of modified JSON

---

# beta

#### General
* [IMP] Code cleanup
* [IMP] UI cleanup

#### Manager
* [VIS] Slot selection: Game Mode icon

#### Editor - Inventory
* [FIX] Item Details: Min/Max Stats for procedural technology seems switched but has a technical background.

#### Editor - Exosuit
* [VIS] Health/Currency icons

#### Editor - Starship
* [FIX] Editor view needs to be reloaded to apply the changed debug mode to the legacy color UI.

#### Editor - Exocraft
* [FIX] Disable+change tab when last one is delete

#### Editor - Freighter
* [FIX] Directly update UI in Frigates when syncing home seed

#### Editor - Knowledge
* [FIX] Directly update UI in Discovery when changing a word

#### Editor - Milestones
* [VIS] Add Icons
