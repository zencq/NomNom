# ROADMAP

* [FIX] = Bugfix
* [VIS] = Visual enhancement
* [FET] = Features
* [IMP] = Improvement of existing feature

---

## General

* [FET] Undo/Redo
* [FET] Backup/Restore (of Inventory/Base)

---

## Manager

* SaveAs
    * [FET] Save current file to other slot
    * [IMP] clearer description about "Save As" and "Save To JSON", maybe combine
* [FET] Backup recovery
* [FET] Delete slot
* [VIS] Slot selection: Game Mode icon

---

## Editor

### Inventory

* [IMP] Unknown Item Handling (Disabled Repair/Install/Details/...)
* Add Items
    * [FET] Ctrl+C, Ctrl+V to copy inventory slots.
    * [FET] Remember last added item
* [FET] Fill chargeable item via right-click
* [FET] Fill all button, etc at the top.
* [FET] Move between Inventories
* [VIS] Tech overloaded
* [VIS] Adjacent bonus color
* [IMP] Rename inventory (for storage container/base)
* [IMP] Select next/previous
* Item Details
    * [IMP] Creation-Group: Rewards (Consumable, Mission, etc.)
    * [FET] Base Building-Group
    * [IMP] Collapse "Dismantle Return" for maintenance items
    * [FET] Frigate-Group
    * [FET] Learnable-group
    * [FIX] Min/Max Stats for procedural technology seems switched but has a technical background.

### Exosuit

* [FET] Customization
* [VIS] Health/Currency icons
* [FET] in-game upgrade cost
* [IMP] show max health

### Starship

* [FET] Customization (Color) -> https://github.com/goatfungus/NMSSaveEditor/issues/231
* [IMP] Allow legacy color for Living ships (no real in-game support as they become pure white).
* [FET] Select active ship
* [FET] Generate Seed for all (EditorView)

### Multitool

* [FET] Customization (Color)
* [FET] Select active weapon
* [FET] Generate Seed for all (EditorView)

### Exocraft

* [FET] Customization (Color)

### Freighter

* [FIX] Directly update UI in Frigates when syncing home seed

### Frigates

* [FET] Delete
* [FET] Copy

### Discovery

* [IMP] learned/total and % complete for words for each race
    * https://github.com/goatfungus/NMSSaveEditor/issues/196
* [IMP] (un)learn all words/Glyphs
* [FET] Unlockable Item Tree
* [FIX] Directly update UI in Discovery when changing a word

### Milestones

* [VIS] Add Icons

### Mission (Log)

* [FET] "^BASE_UPGRADE6" BASE_UPGRADE-Missions have a 1:30h timer.
* [FET] "^BASE_UPGRADE11"-12 (+?) BASE_UPGRADE-Missions have a 6:00h timer.
* [FET] "^???" Living Ship-Missions have a max timer of 24:00h.

---

## JSON Editor

* [FET] Performant TreeView
* [FIX] Proper return of modified JSON

---

## Coordinates

* [FET] List of all own bases/starbase
* [FET] Support for all types of input (hex, glyph, "third one")
* [FET] Enable/Disable portal interference
* [FET] Reset space battle encounter values (TimeLastSpaceBatte + WarpsLastSpaceBattle)
* [FET] Delete TeleportEndpoint

---

## Discovery (useful infos)

* [FET] Starship
    * Inventory when purchase
    * Price (calc by selection, compared to own ships/dif in units to purchase)
    * count per system
* [FET] Farming
    * Grow time
* [FET] Star system
    * Biomes (incl. search for prefix)
    * Is Anomaly in System
    * No of Planets/Moons in System
* [FET] additional stats

---

## Catalogue

* Add Recipe tab
* Group DataGrids
