# CHANGELOG

## 2.4.0.5-alpha.5 (2020-06-13)

* Re-added **Discoveries** tab with new features:
    * Manage your Teleporter Terminus
    * Fast travel to a Teleporter Terminus (Base or Space Station) or any custom
      location with or without your fleet
    * Toggle portal interference
    * Trigger a Freighter battle and show when it would occur naturally
* Changes for **Exocraft**s:
    * Added "Delete Exocraft"
* Added Nexus Mods/Patreon/Reddit as channels in the crash reporter
* Added display of release notes in the notification about new releases
* Added button to reset save path to default
* Updated the internal database to game version 2.52

## 2.2.0.4-alpha.4 (2020-05-17)

* Moved content of **Discoveries** tab to new **Knowledge** tab
* Changes for **Starship**s:
    * Added "Set as current Starship" and "Delete Starship"
    * Changed legacy colors for living ships to be only available in debug mode
* Changes for **Multi-Tool**s:
    * Added "Set as current Multi-Tool" and "Delete Multi-Tool"
    * Added protection against unintended deletion
* Changes for **Exocraft**s:
    * Added renaming
    * Added "Set as current Exocraft"
* Changes for Inventories:
    * Added renaming for Storage Container
    * Added buttons to select the previous/next inventory with a single click
    * Added buttons to enable/repair/fill all slots at once
    * Improved visuals to be even closer to the game
        * Indication for enforced items and those who cannot be deleted in-game
        * Indication for overloaded procedural technology
        * Show adjacent bonus colors

## 2.2.0.3-alpha.3 (2020-04-26)

* Added an integrated updater
* Added an integrated crash report
* Added a new setting to set a custom output path (backups, human-readable JSON
  files, logs, crash reports)
* Improved compatibility for additional Starships, Exocrafts, etc. in future
  game updates which also fixes crashes related to the new Exo Mech when loading
  a save and it's the active Exocraft
* Fixed not updating "Ships Destroyed" milestone when changing its separated
  values
* Fixed a bunch of data type mismatches and other mapping issues in the
  (auto-generated) save file objects that
  [could corrupt a save](https://www.reddit.com/r/NoMansSkyMods/comments/g4e3zv/new_savegame_editor/fo60ja1/)

## 2.2.0.0-alpha.2 (2020-04-19)

* Added logging
* Added **Milestone** tab with all milestones you see in-game

## 2.2.0.0-alpha.1 (2020-04-12)

* First public pre-release
