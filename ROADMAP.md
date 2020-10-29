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

# alpha.14 - Feature Polishing

#### General
* [IMP] Windows Store Platform
    * File Action
    * Trigger Cloud Sync (update containers.index, container.X)
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
    * remove stack size limit
    * skip tech overload check
* [IMP] add platform to crash report
* [IMP] overall improvements and more failsafe
* [IMP] create a first crash report before opening the window. update as before in case there is a user comment
* [IMP] hide unimplemented features instead of disabling them
* [IMP] exception always english
* [IMP] switch back to manager-view (or if possible reload current view on-the-fly)

#### Manager
* [VIS] Slot selection: Game Mode icon
* [IMP] Info why an archive is not compatible
* [FET] Add channels to right down corner (Patreon, discord, etc.)
* [FIX] crash when clicking MS reset

#### Editor - Inventory
* [FET] Move between Inventories
* [FIX] ingredient-only restriction to Ingredient Storage container (check current state)
    * not restricted in debug
* [FET] change product multiplier
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
* [FIX] some resources when you add to a ships inventory (or the base inventory) only lets you set 2 for example the gold.. it should be stacking to 500 in the ship


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

#### Editor - Milestones
* [VIS] Add Icons

#### Catalogue
* [FET] Add Recipe tab
* [IMP] Group DataGrids

---

# alpha.15 - Customization

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

# alpha.16 - More Editor

#### Editor - Knowledge
* [FET] Unlockable Item Tree (+total of CostType to unlock all)

#### Editor - Mission
* [FET] "^BASE_UPGRADE6" BASE_UPGRADE-Missions have a 1:30h timer.
* [FET] "^BASE_UPGRADE11"-12 (+?) BASE_UPGRADE-Missions have a 6:00h timer.
* [FET] "^???" Living Ship-Missions have a max timer of 24:00h.

---

# alpha.17 - Guide

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

# alpha.18 - Clipboard, Store preferences and manually added stats

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

# alpha.19 - Import/Export, Raw JSON

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
    * Not complete but the most relevant data?
* [FET] Change gamemode of a save

#### JSON Editor
* [FET] Unlock
* [FET] Performant TreeView
* [FIX] Proper return of modified JSON

---

# beta

#### General
* [IMP] Code cleanup
* [IMP] UI cleanup

#### Editor - Inventory
* [FIX] Item Details: Min/Max Stats for procedural technology seems switched but has a technical background.
