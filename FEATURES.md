# FEATURES

---

## General

* Multi platform support with automatic detection and indicator.
    * GOG.com (PC)
    * PlayStation
        * Save Mounter
        * SaveWizard
    * Steam (PC)
    * Windows Store (PC)
        * You will get a notification if the game is running as there is a high
          chance that you need to restart it to see the changes.
    * Xbox
        * Only via cloud sync and the Windows Store version.
* Multi language support and changeable at runtime.
    * English
    * German (Deutsch) - currently disabled/derzeit deaktiviert
* Automatic backup of your save file when loaded.
* Save the current save as human-readable JSON.
* Restore a corrupted save if the save data itself are valid by simply saving it
  again.
* Edit multiple saves simultaneously. Select another save without the need to
  save your unsaved changes before.
* Integrated updater.
    * Indicator if you choose to update later.
* Integrated crash reporter.
    * If you encounter a crash please fill out the form with as much information
      as possible that will help fixing it.
    * A report will be automatically stored in your output path.
    * Send me the created data via one of the shown channels (there is a
      button for each one).
* Logging of value changes and other relevant events.
* Custom output path where backups, human-readable JSON files, logs, and
  crash reports are stored. Content will be moved then changed.
* Multiple modes to change behavior:
    * Advanced
        * Enables advanced features that can easily destroy a save if you don't
          know what you are doing.
    * Auto Save
        * Each change will be immediately saved to the disk.
    * Debug
        * Allow adding non-procedural technology more than once to an inventory.
        * Allow legacy colors for living ships (no real in-game support as they
          become pure white).
        * Show save file name in selection.
        * Show IDs in various places and include them in searches.
        * Logging includes debug information.
        * Check for unavailable JSON mapping (included in logging).

---

## Manager

* Select slot and save you want to edit.
    * Slot selection displays play time and last save timestamp of most recent
      save.
    * Save selection displays further details like the type, its game version,
      and some states.
        * **Compatible**: The save is fully compatible and can be loaded for use
          in Editor and Guide pages.
        * **Corrupted**: The save might be compatible but at least the related
          meta information does not match the actual save data. If a save is
          corrupted, it cannot be loaded by the game. In order to fix this, you
          just need to save it with NomNom (even if you haven't changed
          anything). But if the save is also compatible, you can edit it before
          saving if you want to.
        * **Synced**: Indicates whether the current state of the save is the
          same as on the disk.
* Delete, copy, move, or swap your slots (unlocked platform dependent).

---

## Editor

### Inventory

* Resize width and height.
* Enable/Fill/Repair slots individually or all at once.
* Keyboard controls and drag and drop support.
* Visually close to the game itself:
    * Image/Badges and border/background color depending on the item in a slot.
    * Adjacent bonus colors.
    * Indications for not fully installed, damaged, and overloaded tech.
* Lock state indicator to visualize whether an item can be deleted in-game.
* Toggle slot states (enabled, installed, and repaired).
* Add items:
    * Filter via type and category or via free text search.
    * Select the amount you want to add.
    * Select if you want to add technology fully installed or not.
    * Technology that can only be installed once and is already installed will
      be filtered out.
* Show Details:
    * Generic details like name, description, and image.
    * Additional details depending on the actual item:
        * How to acquire it.
        * In which blueprints is it used.
        * Procedural properties depending on type and class.
        * Charging information about what can be used and how much do you need,
          based on the current amount.
        * Technology information like ammo usage, and modifying stats.
        * Trade/Worth information from single value to all inventories.
    * Everything listed in tables can be opened (except the list is disabled)
      to view the details of that item directly.
    * Opened via inventory, the amount and procedural seed can be changed here.
* Delete items (some items cannot be removed as the game will add them back).

### Exosuit

* Toggle 3rd-person cam
* Modify health
* Modify currencies
* Shows if important tech is installed:
    * Haz-Mat Gauntlet
* [Inventory](#inventory)

### Starship

* Toggle 3rd-person cam
* Manage your starfleet:
    * Select your current Starship
    * Delete Starship
* Change Name
* Change Class
* Change Type
* Change Seed
* Change legacy color usage
* Change Base Stats
    * Showing min/max depending on type and class beside the actual value.
* Shows if important tech is installed:
    * Hyperdrive
    * Cadmium Drive
    * Iridium Drive
    * Emeril Drive
    * Conflict Scanner
    * Economy Scanner
* [Inventory](#inventory)

### Multi-Tool

* Manage your arsenal:
    * Select your current Multi-Tool
    * Delete Multi-Tool
* Change Name
* Change Class
* Change Seed
* Change Base Stats
    * Showing min/max depending on type and class beside the actual value.
    * Type cannot be determined via the save itself and must be selected
      manually to show the min/max.
* Shows if important tech is installed:
    * Scanner
    * Analysis Visor
    * Survey Device
    * Advanced Mining Laser
* [Inventory](#inventory)
* Protection against unintended deletion (if you have one without anything in
  the inventory, it will be saved as deleted by the game the next time you save).

### Exocraft

* Toggle 3rd-person cam
* Manage your vehicle fleet:
    * Select your current Exocraft
    * Delete Exocraft (actually resets the location as it cannot be deleted).
* Change Name
* [Inventory](#inventory)

### Freighter

* Change Name
* Change Class
* Change Type
* Change Home System/Model Seed
* Sync home system seed to all frigates
* Change NPC Race/Seed
* Change Base Stats
    * Showing min/max depending on type and class beside the actual value.
* Shows if important tech is installed:
    * Amplified Warp Shielding
    * Chromatic Warp Shielding
    * Temporal Warp Computer
* [Inventory](#inventory)

### Manage Fleet (Frigates)

* Change Name
* Change Class
* Change Type
* Change Home System/Model Seed
* Change NPC Race
* Change Stats
* Change Traits
* Expedition Details:
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
        * Frigates participating on same expedition incl. its condition.
        * Expedition progress.
        * Number of successful events during this expedition.
        * Number of failed events during this expedition.

### Base

* Manage your NPC Worker:
    * Hire
    * Change Seed
* Change Name
    * Also changes name of the related Teleport Terminus.
* Summon NPC Worker to current base.
* Show item count and upload-limit.
* Toggle cylindrical rooms (Room <-> Frame).
    * You cannot place ladders in frames in-game but still move through them if
      a ladder is inside.
* Clear Terrain edits (of the whole planet).
* Move Base Computer
    * Delete or rename the related Teleport Terminus.
    * A new Teleport Terminus entry will be added as soon as you visit the base.
* [Storage Container](#inventory)
    * Change Name

### Discoveries

* Manage your Teleport Terminus:
    * Delete
* Change Name of Teleport Terminus
* Show galaxy, coordinates, glyphs and distances
* Fast travel to a Teleport Terminus or any custom location with or without your
  fleet
* Toggle Portal Interference
* Trigger a Freighter battle and show when it would occur naturally

### Knowledge

* Technology
* Products
* Quicksilver Synthesis Companion
* Words
* Glyphs

### Milestones

* Journey Milestones
    * Learned words are updated when you change a related value in
      [Knowledge](#knowledge) tab.
    * Cumulated kills are shown as separate values.
* The Gek
* The Vy'keen
* The Korvax
* Merchants Guild
* Mercenaries Guild
* Explorers Guild

---

## Catalogue

* List of all technologies, products and substances.
* Each will show it's details (see [Inventory](#inventory)/Show Details).
