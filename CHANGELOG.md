# CHANGELOG

All notable changes to this project will be documented in this file. The format
is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) and uses its
[own versioning](README.md#versioning).

## 3.0.0.11-alpha.11 (2020-10-07)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.0.0.11-alpha.11/total)

### Fixed
* Some incompatibility issues
* A bug that could cause PS4 saves to become corrupted while saving
* [GitHub issues](https://github.com/cengelha/NomNom/issues) [#18](https://github.com/cengelha/NomNom/issues/18) [#19](https://github.com/cengelha/NomNom/issues/19) [#20](https://github.com/cengelha/NomNom/issues/20) [#23](https://github.com/cengelha/NomNom/issues/23)

## 3.0.0.10-alpha.10 (2020-10-04)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.0.0.10-alpha.10/total)

### Fixed
* [GitHub issue](https://github.com/cengelha/NomNom/issues) [#17](https://github.com/cengelha/NomNom/issues/17)

## 3.0.0.9-alpha.9 (2020-10-04)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.0.0.9-alpha.9/total)

### Fixed
* A few incompatibility issues
* A crash that could occur on startup
* [GitHub issues](https://github.com/cengelha/NomNom/issues) [#13](https://github.com/cengelha/NomNom/issues/13) [#16](https://github.com/cengelha/NomNom/issues/16)

## 3.0.0.8-alpha.8 (2020-10-04)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.0.0.8-alpha.8/total)

### Changed
* Updated the internal database to game version 3.02
* Toggle for portal interference only visible for game versions below 3.0

### Fixed
* A few bugs that caused a crash when adding a new item to an inventory
* Changing starship type to Living now works properly

## 2.6.0.7-alpha.7 (2020-09-29)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/2.6.0.7-alpha.7/total)

### Added
* Support for the following platforms (see [README](README.md#requirements) for
  details):
    * PlayStation (Save Mounter) ([#8](https://github.com/cengelha/NomNom/issues/8))
    * Windows Store
    * Xbox (via Windows Store cloud sync)
* New fleet stat for freighter for 2.6 and up

### Changed
* Updated the internal database to game version 2.62
* Technology can now be installed in freighter's general inventory with game
  version 2.6 and up
* If a save is to old to be supported you get that as log entry instead of a
  most likely appearing error
* NomNom now supports Beyond (2.14) and up

### Fixed
* Loading unsupported files should no longer crash
* [GitHub issue](https://github.com/cengelha/NomNom/issues) [#9](https://github.com/cengelha/NomNom/issues/9)

## 2.4.0.6-alpha.6 (2020-08-28)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/2.4.0.6-alpha.6/total)

### Added
* Indicator if a new update is available but you choose to update later
* Navigation area can be collapsed and you can select a default landing page
* Support for the following platforms of the game (see
  [README](README.md#requirements) for details):
    * PlayStation (SaveWizard)
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
* [GitHub issues](https://github.com/cengelha/NomNom/issues) [#1](https://github.com/cengelha/NomNom/issues/1) [#2](https://github.com/cengelha/NomNom/issues/2) [#3](https://github.com/cengelha/NomNom/issues/3) [#5](https://github.com/cengelha/NomNom/issues/5)

## 2.4.0.5-alpha.5 (2020-06-13)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/2.4.0.5-alpha.5/total)

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
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/2.2.0.4-alpha.4/total)

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
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/2.2.0.3-alpha.3/total)

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
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/2.2.0.0-alpha.2/total)

### Added
* Logging
* **Milestone** tab with all milestones you see in-game

## 2.2.0.0-alpha.1 (2020-04-12)

* First public pre-release
