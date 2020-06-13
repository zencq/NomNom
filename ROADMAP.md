# ROADMAP

This order could be changed due to new game updates.

### Legend
* [FET] = New features
* [FIX] = Bugfix
* [IMP] = Improvements for existing features
* [VIS] = Visual enhancement

---

# alpha.6

#### General
* [IMP] Handling of customization technology

#### Editor - Exosuit
* [FET] Customization

#### Editor - Starship
* [FET] Customization (https://github.com/goatfungus/NMSSaveEditor/issues/231)

#### Editor - Multi-Tool
* [FET] Customization

#### Editor - Exocraft
* [FET] Customization

---

# alpha.7

#### General
* [IMP] some UI changes

#### Editor - Inventory
* [FET] Move between Inventories
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

#### Editor - Frigates
* [FET] Copy
* [FET] Delete

#### Editor - Discoveries
* [FET] Delete TerrainEdit of any planet

#### Editor - Knowledge
* [IMP] learned/total and % complete for words for each race (https://github.com/goatfungus/NMSSaveEditor/issues/)196
* [IMP] (un)learn all

---

# alpha.8

#### Editor - Knowledge
* [FET] Unlockable Item Tree (+total of CostType to unlock all)

#### Editor - Mission
* [FET] "^BASE_UPGRADE6" BASE_UPGRADE-Missions have a 1:30h timer.
* [FET] "^BASE_UPGRADE11"-12 (+?) BASE_UPGRADE-Missions have a 6:00h timer.
* [FET] "^???" Living Ship-Missions have a max timer of 24:00h.

---

# alpha.9

#### General
* [IMP] Integrate both paths in menu

#### Manager
* SaveAs
    * [FET] Save current file to other slot
    * [IMP] clearer description about "Save As" and "Save To JSON", maybe combine
* [FET] Backup recovery
* [FET] Swap save slots
* [FET] Delete slot
* [FIX] Changes in files detection

---

# alpha.10

#### Catalogue
* [FET] Add Recipe tab
* [IMP] Group DataGrids

---

# alpha.11

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
    * Biomes (incl. search for prefix)
    * Is Anomaly in System
    * No of Planets/Moons in System
* [FET] additional stats

---

# alpha.12

#### General
* [FET] Undo/Redo
* [IMP] Left/Right sidebars collapsible
* [FET] remember various tool states (last added item [inventory], sidebars collapsed, selected tab, etc)
* [FET] new mode to select if the various states above should be remember across multiple sessions

#### Editor - Inventory
* [FET] Ctrl+C, Ctrl+V to copy inventory slots.

#### Editor - Multi-Tool
* [FET] store Type selection (of seed)

#### Editor - Discoveries
* [FET] Store manual TeleportEndpoint
* [FET] remember last enter ly distance for jumps to center

---

# alpha.13

#### General
* [FET] Backup/Restore (of Inventory/Starship/Base/etc)

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
