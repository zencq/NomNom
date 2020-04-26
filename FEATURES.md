# FEATURES

---

## General

* Integrated updater.
* Custom output path where backups, JSON files, logs, and crash reports are
  stored.
* Automatic backup of your save file when loaded.
* Logging of value changes and other relevant events.
* Integrated crash reporter.
    * If you encounter a crash please fill out the form with as much information
      as possible that will help fixing it.
    * A report will be automatically stored in your output path.
    * Create a [GitHub issue](https://github.com/cengelha/NomNom/issues) or send
      an email with the data attached.
* Multi language support.
  * English
  * German
* Multiple modes to change behavior:
    * Advanced
        * Enables advanced features that can easily destroy a save if you don't
          know what you are doing.
    * Auto Save
        * Each change will be immediately saved to the disk.
    * Debug
        * Show IDs in various places and include them in searches.
        * Allow adding non-procedural technology more than once to an inventory.
        * Logging includes debug information.
        * Check for unavailable JSON mapping (included in logging).

---

## Manager

* Select the slot and file you want to edit.
* Save the selected file to an human readable JSON file.
* Restore corrupted saves (if you manually edited the storage file [save.hg]).

---

## Editor

### Inventory

* Built to mirror the games data as much as possible.
* Resize width and height.
* Move items via drag and drop.
* Toggle slots (Enable/Disable, Fully Installed/Needs Repair/Needs Installation).
* Add items
    * Filter an item manually via type and category or via free text search.
    * Select the amount you want to add.
    * Select if you want add technology fully installed or not.
    * Technology that can only be installed once and is already installed will
      be filtered out.
* Delete items (some items cannot be removed as the game will add them back).
* Show Details
    * Generic details like name and description.
    * Additional details depending on the actual item:
        * Procedural properties (incl. min/max for each stat depending on type
          and class).
        * How to acquire it.
        * Charge information (what can be used and how much do I need).
        * In which blueprints is it used.
        * Technology information (ammo, deploying into, modified stats, etc).
        * Trade/Worth information (from single value over the current inventory
          to all inventories).
    * Everything listed in tables can be opened (except the list is disabled)
      to view the details directly.
    * Opened via inventory, the amount and procedural seed can be changed here.

### Exosuit

* Toggle 3rd-person cam
* Modify health
* Modify currencies
* Show if important tech is installed:
    * Haz-Mat Gauntlet
* [Inventory](#inventory)

### Starship

* Toggle 3rd-person cam
* Delete Starship
* Change Name
* Change Class
* Change Type
* Change Seed
* Use Legacy Colors
* Base Stats
    * Showing min/max stats for the type and class beside the actual value.
* Show if important tech is installed:
    * Hyperdrive
    * Cadmium Drive
    * Iridium Drive
    * Emeril Drive
    * Conflict Scanner
    * Economy Scanner
* [Inventory](#inventory)

### Multitool

* Delete Multitool
* Change Name
* Change Class
* Change Seed
* Base Stats
    * Showing min/max stats for the type and class beside the actual value.
    * Type cannot be determined via the save itself and must be selected
      manually to show the min/max.
* Show if important tech is installed:
    * Scanner
    * Analyis Visor
    * Survey Device
    * Advanced Mining Laser
* [Inventory](#inventory)

### Exocraft

* Toggle 3rd-person cam
* [Inventory](#inventory)

### Freighter

* Change Name
* Change Class
* Change Type
* Change Home/Model Seed
    * Sync Freighter Home-Seed to all frigates.
* Change NPC Race/Seed
* Base Stats
    * Showing min/max stats for the type and class beside the actual value.
* Show if important tech is installed:
    * Amplified Warp Shieldung
    * Chromatic Warp Shieldung
    * Temporal Warp Computer
* [Inventory](#inventory)

### Frigates

* Change Name
* Change Class
* Change Type
* Change Home/Model Seed
* Change NPC Race
* Change Stats
* Change Traits
* Expedition Details
    * Total of finished expeditions.
        * Fast forward so next expedition will trigger a level-up.
        * How much expeditions are necessary for the next level-up.
        * Number of remaining level-ups.
    * Total of successful events during expeditions.
    * Total of failed events during expeditions.
    * Total of times damaged.
    * Current state (idle, damaged, on expedition, etc.)
        * Successful finish current expedition.
        * Repair frigate.
    * Information about an ongoing expedition
        * Type of expedition.
        * Frigates participating on same expedition (incl. it's condition).
        * Expedition progress.
        * Number of successful events during this expedition.
        * Number of failed events during this expedition.

### Base

* Change Name
* NPC Worker
    * Change seed.
    * Summon to current base.
* Show item count and upload-limit.
* Clear TerrainEdit (of whole planet).
* Toggle cylindrical rooms (Room <-> Frame) as you can't place ladders in frames
  but still move through them if a ladder is inside.
* Move Base Computer
    * Delete or rename old TeleportEndpoint.
    * New TeleportEndpoint will be added as soon as you visit the base.
* Storage Container [Inventory](#inventory)

### Discovery

* Technology
* Products
* Quicksilver Synthesis Companion Products
* Glyphs
* Words

### Milestones

* Journey Milestones
    * Learned words are updated when you change a related value in __Discovery__
      tab.
    * Cumulated kills are shown as separate values.
* The Gek
* The Vy'keen
* The Korvax
* Merchants Guild
* Mercenaries Guild
* Explorers Guild

---

## Coordinates

---

## Catalogue

* List of all technologies, products and substances.
* Each will show it's details (see [Inventory](#inventory)/Show Details).
