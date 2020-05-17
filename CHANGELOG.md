# CHANGELOG

<!--
## 2.2.0.5-alpha.5 (2020-05-??)

* Added teleport endpoint management, fast travel and other related features in
  __Discoveries__ tab
* Display changelog in new version notification
*
I also started a Patreon page if you want to support me but also as little developer's diary to keep you updated.
 -->

## 2.2.0.4-alpha.4 (2020-05-17)

* Moved content of __Discoveries__ tab to new __Knowledge__ tab
* __Starship__
    * Legacy colors for living ships only in debug mode
    * Activated "Set as current Starship" and "Delete Starship"
    * UI now closer to what could be the final look. __Let me know what you
      think__
* Inventory
    * Naming for storage container
    * Button to enable/repair/fill all slots at once
    * Visually even closer to the game
    * Indication for enforced items and those who cannot be deleted in-game
    * Indicate overloaded procedural technology
    * Show adjacent bonus colors
    * Select previous/next inventory with a single click
* __Multi-Tool__
    * Activated "Set as current Multi-Tool" and "Delete Multi-Tool"
    * Protection against unintended deletion (if you save without at least one
      item in the inventory the game will delete it)
* __Exocraft__
    * Naming
    * Activated "Set as current Exocraft"

## 2.2.0.3-alpha.3 (2020-04-26)

* Added an integrated updater
* Added an integrated crash reporter
* Added a setting to select a custom path for output (backups, human-readable
  JSON files, logs, crash reports)
* Improved compatibility for additional Starships, Exocrafts, etc. in future
  game updates which also fixes crashes related to the new Exo Mech when loading
  a save
* Fix for not updating "Ships Destroyed" milestone when changing its separated
  values
* Fixed a bunch of data type mismatches and other mapping issues in the
  (auto-generated) save file object that could
  [potentially corrupt a save](https://www.reddit.com/r/NoMansSkyMods/comments/g4e3zv/new_savegame_editor/fo60ja1/)

## 2.2.0.0-alpha.2 (2020-04-19)

* Added logging
* Added __Milestone__ tab with everything you see in-game

## 2.2.0.0-alpha.1 (2020-04-12)

* First public pre-release
