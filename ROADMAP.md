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

# alpha.8 - Origins Update

* [IMP] New Mappings
???
    "ux@": {
???
    "CYJ": [],
???
    "6Ws": 0,
PhotoModeSettings
    "wKU": 0,
    "RUO": 2.0,
    "yuu": 200.0,
    "n0h": 5.0,
    ">xF": 200.0,
???
    "ym>": [
    "uK6": [
    "2jw": 0,
    "J3C": [
    "OYB": false

* [INF] New cooking products have been added, reflecting the range of novel meats and other sustainably harvested ingredients made possible by the new creature types.

* [INF] During storms, the Exosuit can now take advantage of the extreme conditions: superheated temperatures can be processed into improved jetpack efficiency; freezing temperatures prevent Mining Beam overheating; high radioactivity increases mining yield; dense toxic gases can be recirculated for additional stamina.

* [INF] These traders sell a range of exotic goods, including black-market upgrade modules.
* [INF] The scrap dealer found about space stations will now exchange pugneum for rare or exotic contraband items.

* [INF] The number of items in an inventory stack is now displayed in the popup header.

* [INF] A number of lesser-used crafting products have been removed from the game.
* [INF] A smaller number of new crafting products have been added to replace them.
* [INF] The number of specialist survival products have been reduced. The stack size for the remaining survival products has been increased.
* [INF] The stack size for Glass has been increased.
* [INF] A range of new buried items have been added to planets. These can be found and processed to reveal a range of exotic and interesting new items.

* [INF] Multi-Tools can now be upgraded at the Multi-Tool technology merchant aboard most Space Stations.
* [INF] New inventory slots can be added, up to a maximum size for the current class. These slots cost a large number of units.
* [INF] Multi-Tool class can also be upgraded for a significant amount of nanites.
* [INF] Multi-Tool Expansion Slots allow the addition of an inventory slot for free. Find these upgrade circuits while exploring planets.

* [INF] Portal interference for conventional portals has been removed. Players may explore freely.
* [INF] After going through a portal, the return portal will remain active until you leave the planet. Your previous system is added to the list of available destinations at the space station teleporter.

---

# alpha.9 - Editor Feature Polishing

#### General
* [IMP] Windows Store Platform
    * File Action
    * Trigger Cloud Sync (update containers.index, container.X)
* [IMP] Notification is saving finished
* [IMP] Info why an archive is not compatible
* [IMP] Integration of libMBIN
* [IMP] some UI changes
* [IMP] Handling of customization technology
    * add the "^T_<id>" in KnownTech and "^<id>" in KnownSpecials
    * METADATA/GAMESTATE/PLAYERDATA/BOBBLEHEADCUSTOMISATIONDATA.EXML
    * METADATA/GAMESTATE/PLAYERDATA/THRUSTERCUSTOMISATIONDATA.EXML
* [IMP] Seed mode to set seed as name too (or separate button)
* [IMP] Naming and handling of procedural items

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
* [FET] clear space station exosuit interaction

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

# alpha.10 - Customization

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

# alpha.11 - More Editor

#### Editor - Knowledge
* [FET] Unlockable Item Tree (+total of CostType to unlock all)

#### Editor - Mission
* [FET] "^BASE_UPGRADE6" BASE_UPGRADE-Missions have a 1:30h timer.
* [FET] "^BASE_UPGRADE11"-12 (+?) BASE_UPGRADE-Missions have a 6:00h timer.
* [FET] "^???" Living Ship-Missions have a max timer of 24:00h.

---

# alpha.12 - Catalogue Polishing

#### Catalogue
* [FET] Add Recipe tab
* [IMP] Group DataGrids

---

# alpha.13 - Guide

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

# alpha.14 - Clipboard, Store preferences and manually added stats

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

# alpha.15 - Import/Export, Raw JSON

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
    * Not complete but the most relevant data

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
