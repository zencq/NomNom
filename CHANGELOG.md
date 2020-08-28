# CHANGELOG

All notable changes to this project will be documented in this file. The format
is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) and uses its
[own versioning](README.md#versioning).

<!-- ## Unreleased

### Added
* Support for the following platforms (see [README](README.md#requirements) for
  details):
    * Windows Store (detection only for now)
* New fleet stat for freighter

### Changed
* Updated the internal database to game version 2.62
* Technology can now be installed in freighter's general inventory -->

## 2.4.0.6-alpha.6 (2020-08-28)

### Added
* Indicator if a new update is available but you choose to update later
* Navigation area can be collapsed and you can select a default landing page
* Support for the following platforms of the game (see
  [README](README.md#requirements) for details):
    * PlayStation 4 (SaveWizard)
* Platform indicator
* Reset buttons to the default save path of each PC platform
* Slot management: delete, copy, move, and swap (unlocked platform dependent)
* Game version of a save in the manager page
* It's now possible to edit multiple saves at once (see
  [FEATURES](FEATURES.md#manager) for details)

### Changed
* Moved all current buttons to the menu
* Enhanced Crash Reporter with directly showing the installed .NET version and
  recursive InnerException for better and more information to fix the crash
* Upgraded to .NET Framework 4.8

### Fixed
* Detection of external changes
* Debug logging switch works without restart now
* [GitHub issues](https://github.com/cengelha/NomNom/issues) [#1](https://github.com/cengelha/NomNom/issues/3) [#2](https://github.com/cengelha/NomNom/issues/3) [#3](https://github.com/cengelha/NomNom/issues/3) [#5](https://github.com/cengelha/NomNom/issues/5)

## 2.4.0.5-alpha.5 (2020-06-13)

### Added
* Re-added **Discoveries** tab with new features:
    * Manage your Teleporter Terminus
    * Fast travel to a Teleporter Terminus (Base or Space Station) or any custom
      location with or without your fleet
    * Toggle portal interference
    * Trigger a Freighter battle and show when it would occur naturally
* "Delete Exocraft"
* Nexus Mods/Patreon/Reddit as channels in the crash reporter
* Display of release notes in the notification about new releases
* Button to reset save path to default

### Changed
* Updated the internal database to game version 2.52

## 2.2.0.4-alpha.4 (2020-05-17)

### Added
* "Set as current Starship" and "Delete Starship"
* "Set as current Multi-Tool" and "Delete Multi-Tool"
* Protection against unintended deletion for Multi-Tools
* "Set as current Exocraft" and renaming of Exocrafts
* Renaming for Storage Container
* Buttons to select the previous/next inventory with a single click
* Buttons to enable/repair/fill all slots at once

### Changed
* Moved content of **Discoveries** tab to new **Knowledge** tab
* Changed legacy colors for living ships to be only available in debug mode
* Improved visuals to be even closer to the game:
    * Indication for enforced items and those who cannot be deleted in-game
    * Indication for overloaded procedural technology
    * Show adjacent bonus colors

## 2.2.0.3-alpha.3 (2020-04-26)

### Added
* Integrated updater
* Integrated crash report
* A new setting to set a custom output path (for backups, human-readable JSON
  files, logs, and crash reports)

### Changed
* Improved compatibility for additional Starships, Exocrafts, etc. in future
  game updates which also fixes crashes related to the new Exo Mech when loading
  a save and it's the active Exocraft

### Fixed
* Not updating "Ships Destroyed" milestone when changing its separated
  values
* A bunch of data type mismatches and other mapping issues in the
  (auto-generated) save file objects that
  [could corrupt a save](https://www.reddit.com/r/NoMansSkyMods/comments/g4e3zv/new_savegame_editor/fo60ja1/)

## 2.2.0.0-alpha.2 (2020-04-19)

### Added
* Logging
* **Milestone** tab with all milestones you see in-game

## 2.2.0.0-alpha.1 (2020-04-12)

* First public pre-release
