# CHANGELOG

All notable changes to this project will be documented in this file. It uses the
[Keep a Changelog](http://keepachangelog.com/en/1.0.0/) principles and its
[own versioning](README.md#versioning).

## Unreleased

### Known Issues
### Added
### Changed
### Removed
### Fixed

## 4.00.0.31-beta.1 (2022-10-31)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/4.00.0.31-beta.1/total)

### Added
* Support for **Waypoint 4.0** ([#95](https://github.com/cengelha/NomNom/issues/95) [#98](https://github.com/cengelha/NomNom/issues/98))
* Name and Summary of a save
* Difficulty Presets
* Switch early adopter Starship and Multi-Tool
* Maneuverability for Starships
* Supercharged technology
* Support for Nintendo Switch saves ([#96](https://github.com/cengelha/NomNom/issues/96))
* Welcome window for first-time users
* Mod support! Customize the look and feel/behavior according to the mods you use. See [here](https://github.com/cengelha/NomNom/wiki) for more information
* Menu items to directly open most important directories in File Explorer
* New settings (window) including loading strategy, window attributes (position and size), and more
* Multi-language support starting with German and Korean
* New setting for additional paths that will be checked like other default locations (useful for console saves)
* Automatic detection of platforms in the default location of a platform
* Built-in backup recovery ([#57](https://github.com/cengelha/NomNom/issues/57))
* Button to show why a save is incompatible
* Option to hide backups and incompatible saves from the list
* JSON editor: Tree view including a search
* JSON editor: Diff view (for performance reasons only for account data for now)
* JSON editor: Export and import the current snippet
* JSON editor: Search for the tree view
* Integration of Inventory Transfer to the [Assistant for No Man's Sky](https://nmsassistant.com/) app
* Duplicate inventory slots and cache last item added
* Remaining images of all items
* Live Community Research progress in the respective tabs
* Username is now displayed in the title names if one was found in loaded saves
* Filter and buttons to (un)lock multiple items at once
* Buttons to increase currencies to its maximum
* Tainted Metal to currencies (read-only)
* The total play time is now editable in General tab
* Manage your collections
    * Open JSON of selection directly
    * Pre-filled with pre-order, starter, expedition, and Twitch rewards
* Integration of the Discord [Creative & Sharing Hub](https://discord.gg/RSGQFQv2pP)
    * Open respective channels to share or find new things from/for your collections
    * Open the Customizer directly in NomNom (you still have to use the Discord to get the seeds)
* Resources can be edited via UI in Advanced Mode
* Icons of are now displayed in technology overviews
* Display which interior adornment and exhaust override is visible in a Starship
* Squadrons can now be edited
* Toggle Mech AI Pilot
* Missing items in the catalogue (e.g. Shroud of Freedom) and filter options ([#84](https://github.com/cengelha/NomNom/issues/84))
* Show total object count of all bases compared to allowed max ([#56](https://github.com/cengelha/NomNom/issues/56))
* Single Base Building Objects added to the Teleporter list
* Analysis of how many words are learned per category and race
* Showing in-game descriptions for companion traits
* Command line interface to convert files similar to the new import/export feature
* and proably more...

### Changed
* Upgrade to .NET 6
* Use libMBIN mapping.json including automatic (and manual) updates
    * Updating the mapping automatically applies all new entries (if any) to all loaded files
* Updated UI and code cleanup and optimization
* Actions to delete/copy/move/swap slots are now available as individual buttons in the list
* JSON editor available for saves older than Beyond 2.11
* Save Transfer is now an independent wizard where you can select source and destination freely as well as what you want to transfer ([#61](https://github.com/cengelha/NomNom/issues/61))
* Transformed "Save as JSON" to a import/export feature. You can import any valid human- or game-readable file
* Max health is determined by game parameter and install tech (proc tech only approx if [Pi](https://github.com/zencq/Pi) isn't present)
* Type of Multi-Tool is now pre-determined by collection, resource, and stats (based on the intended ranges) if possible
* Exocraft tab always accessible and showing whether one was already deployed
* Unlocked various seeds for companions even if currently not used
* Amount to add to inventory slot can now be modified directly additional to the slider ([#85](https://github.com/cengelha/NomNom/issues/85))
* Filtering for items to add to inventory slot ([#94](https://github.com/cengelha/NomNom/issues/94))
* and proably more...

### Fixed
* Base selection did not update data properly ([#74](https://github.com/cengelha/NomNom/issues/74))
* Multiple crashes should be resolved ([#76](https://github.com/cengelha/NomNom/issues/76) [#87](https://github.com/cengelha/NomNom/issues/87) [#92](https://github.com/cengelha/NomNom/issues/92))
* and a lot of other things...

## 3.94.0.30-alpha.30 (2022-07-30)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.94.0.30-alpha.30/total)

### Added
* Organic frigate type
* Cargo inventory for freighters
### Changed
* Updated name mapping to game version 3.97
* Updated database to game version 3.98

## 3.90.0.29-alpha.29 (2022-05-26)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.90.0.29-alpha.29/total)

### Added
* Leviathan frigate type
### Changed
* Updated name mapping to game version 3.90
* Updated database to game version 3.90

## 3.85.0.28-alpha.28 (2022-05-19)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.85.0.28-alpha.28/total)

### Fixed
* Issues with the Microsoft platform including [#79](https://github.com/cengelha/NomNom/issues/79) and [#83](https://github.com/cengelha/NomNom/issues/83)

## 3.85.0.27-alpha.27 (2022-04-24)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.85.0.27-alpha.27/total)

### Added
* Solar Sail as ship type ([#82](https://github.com/cengelha/NomNom/issues/82))
* Cargo inventory for ships
### Changed
* Updated name mapping to game version 3.87
* Updated database to game version 3.87

## 3.8.0.26-alpha.26 (2022-02-28)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.8.0.26-alpha.26/total)

### Fixed
* Crash when save does not contain the new weapon resource
* `Extreme Survival` milestone not calculating correctly ([#78](https://github.com/cengelha/NomNom/issues/78))
* Some Frigate types not being displayed and set correctly

## 3.8.0.25-alpha.25 (2022-02-24)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.8.0.25-alpha.25/total)

### Added
* Royal as weapon type
### Changed
* Updated name mapping to game version 3.82
* Updated database to game version 3.82
### Fixed
* Exocraft unlock logic (unintentionally checked only the Roamer)

## 3.7.0.24-alpha.24 (2022-01-03)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.7.0.24-alpha.24/total)

### Fixed
* Crash related to expeditions saves
* Tooltip for Companion actions (Delete + Reset Customization)
* An issue with internationalization assets

## 3.7.0.23-alpha.23 (2021-12-22)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.7.0.23-alpha.23/total)

### Added
* `Settlement` tab for editing settlements
### Changed
* New save format for PlayStation is loaded first now and old `memory.dat` only if no new is available
### Fixed
* Detecting/reading of older expedition save data

## 3.7.0.22-alpha.22 (2021-12-11)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.7.0.22-alpha.22/total)

### Added
* `Expedition` tab for editing the progress
### Changed
* Moved learning words to `Milestones` tab incl. some optimizations
### Fixed
* Expedition `Beachhead Redux` and up not correctly displayed/handled
* An issue when processing the meta file ([#63](https://github.com/cengelha/NomNom/issues/63) [#68](https://github.com/cengelha/NomNom/issues/68))

## 3.7.0.21-alpha.21 (2021-12-06)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.7.0.21-alpha.21/total)

### Changed
* Editor button naming to avoid confusion
* Tab order and naming
### Fixed
* Exception in get_IsAccountUnlocked
* Some issues with the Microsoft platform

## 3.7.0.20-alpha.20 (2021-11-28)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.7.0.20-alpha.20/total)

### Added
* Golden Vector as starship type
* `Synthesis Companion` tab for Quicksilver items, Season Rewards, and Twitch Rewards
* Cross-save editing for all platforms **except** PlayStation (SaveWizard does not convert `SAVEDATA00`)
* JSON Editor for account data
* `General` tab to change game mode ([#12](https://github.com/cengelha/NomNom/issues/12))
* `Companion` tab for editing companions
    * Moods, Seeds, Traits, and more...
### Changed
* Updated name mapping to game version 3.74 (base on [MBINCompiler mapping file](https://github.com/monkeyman192/MBINCompiler/releases/download/v3.73.0-pre1/mapping.json))
* Updated database to game version 3.74
* Moved JSON editor to left side bar
* Moved currencies to new `General` tab
### Fixed
* Knowledge tab now working as intended ([#30](https://github.com/cengelha/NomNom/issues/30) [#58](https://github.com/cengelha/NomNom/issues/58))
* Various issues when accessing values from the save
* Properly writing account data and settings back to containers.index (Microsoft platform only)

## 3.6.0.19-alpha.19 (2021-10-28)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.6.0.19-alpha.19/total)

### Added
* Compatibility with the new save format for PlayStation

### Changed
* Updated name mapping to game version 3.6
* Manager now shows from which expedition a save is

### Fixed
* An issue with expeditions saves and the new save format
* An issue on Microsoft platform with a high slot count

## 3.6.0.18-alpha.18 (2021-09-04)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.6.0.18-alpha.18/total)

### Added
* Compatibility with the new save streaming system on Steam

### Fixed
* Not changing ship seed

## 3.5.0.17-alpha.17 (2021-08-25)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.5.0.17-alpha.17/total)

### Added
* Button to remove all external/visited bases from your save
* Raw JSON editor in a plain version without tree
* Hint for procedural item repo (https://github.com/zencq/Pi)
* Saves can be transferred to another platform (between any supported) or to a different account within the same platform

### Changed
* Updated database to game version 3.53
* Forced suit tech is now locked if there is only one in all suit inventories (was always locked before)

### Fixed
* A multi-threading issue when loading the saves
* A bug when saving a Micorsoft platform save if a deleted but unsynced save is present
* A crash when the `containers.index` of Microsoft platform contains wrong data for a single save
* Not being in ship after teleportation
* When switching between regular/living ship types not being asked for confirmation, tech not being replacement, and listing the wrong tech if you want to add some directly afterwards
* Wrong max amount when adding an item to an inventory

## 3.1.0.16-alpha.16 (2021-06-26)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.1.0.16-alpha.16/total)

### Added
* Create/Delete operations for Windows Store saves
* Windows Store cloud sync can be triggered now at any time by closing the game. No need to load and save a savegame anymore.
* Links to different channels to find help or to support the development of NomNom

### Changed
* Mapping matches [MBINCompiler](https://github.com/monkeyman192/MBINCompiler) naming again
* Copy/Move/Swap is still triggered on slots but the actual action is decided for each save
* Redefined version checking and now officially supporting 2.11 an up
* Settings are now stored portable right next to the executable
* Removed "Corrupted" checkbox as it is now merged into the "Compatible" one

### Fixed
* Crashes that mostly occurred on startup ([#31](https://github.com/cengelha/NomNom/issues/31) [#32](https://github.com/cengelha/NomNom/issues/32) [#34](https://github.com/cengelha/NomNom/issues/34) [#43](https://github.com/cengelha/NomNom/issues/43) [#45](https://github.com/cengelha/NomNom/issues/45) [#50](https://github.com/cengelha/NomNom/issues/50))
* Vanishing data and other incompatibility issues ([#35](https://github.com/cengelha/NomNom/issues/35) [#41](https://github.com/cengelha/NomNom/issues/41) [#44](https://github.com/cengelha/NomNom/issues/44) [#49](https://github.com/cengelha/NomNom/issues/49))

## 3.1.0.15-alpha.15 (2020-11-12)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.1.0.15-alpha.15/total)

### Changed
* Updated the internal database to game version 3.10

## 3.0.0.14-alpha.14 (2020-10-29)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.0.0.14-alpha.14/total)

### Changed
* Updated the internal database to game version 3.05

## 3.0.0.13-alpha.13 (2020-10-13)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.0.0.13-alpha.13/total)

### Fixed
* Even more incompatibility issues ([#28](https://github.com/cengelha/NomNom/issues/28))
* A bug that caused procedural tech to be added as not fully installed

## 3.0.0.12-alpha.12 (2020-10-09)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.0.0.12-alpha.12/total)

### Fixed
* Some incompatibilities for older versions and some saves which have the newly added PlanetaryMappingData key in it ([#26](https://github.com/cengelha/NomNom/issues/26))

## 3.0.0.11-alpha.11 (2020-10-07)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.0.0.11-alpha.11/total)

### Fixed
* More incompatibility issues ([#18](https://github.com/cengelha/NomNom/issues/18) [#19](https://github.com/cengelha/NomNom/issues/19) [#20](https://github.com/cengelha/NomNom/issues/20))
* A bug that could cause PS4 saves to become corrupted while saving
* A crash when viewing item details ([#23](https://github.com/cengelha/NomNom/issues/23))

## 3.0.0.10-alpha.10 (2020-10-04)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.0.0.10-alpha.10/total)

### Fixed
* A bug introduced while fixing the previous incompatibility issues ([#17](https://github.com/cengelha/NomNom/issues/17))

## 3.0.0.9-alpha.9 (2020-10-04)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/3.0.0.9-alpha.9/total)

### Fixed
* Incompatibility issues ([#13](https://github.com/cengelha/NomNom/issues/13) [#16](https://github.com/cengelha/NomNom/issues/16))
* A crash that could occur on startup

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
    * PlayStation 4 (Save Mounter) ([#8](https://github.com/cengelha/NomNom/issues/8))
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
* Loading unsupported files should no longer crash ([#9](https://github.com/cengelha/NomNom/issues/9))

## 2.4.0.6-alpha.6 (2020-08-28)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/2.4.0.6-alpha.6/total)

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
* Crashes on startup or when opening the editor ([#1](https://github.com/cengelha/NomNom/issues/1) [#2](https://github.com/cengelha/NomNom/issues/2) [#3](https://github.com/cengelha/NomNom/issues/3) [#5](https://github.com/cengelha/NomNom/issues/5))

## 2.4.0.5-alpha.5 (2020-06-13)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/2.4.0.5-alpha.5/total)

### Added
* Re-added **Discoveries** tab with new features:
    * Manage your Teleporter Terminus
    * Fast travel to a Teleporter Terminus (Base or Space Station) or any custom
      location with or without your fleet
    * Toggle portal interference
    * Trigger a Freighter battle and show when it would occur naturally
* For Exocrafts "Delete"
* Nexus Mods/Patreon/Reddit as channels in the crash reporter
* Display of release notes in the notification about new releases
* Button to reset save path to default

### Changed
* Updated the internal database to game version 2.52

## 2.2.0.4-alpha.4 (2020-05-17)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/2.2.0.4-alpha.4/total)

### Added
* For Starships "Set as current" and "Delete"
* For Multi-Tools "Set as current" and "Delete"
* Protection against unintended deletion of Multi-Tools
* Renaming for Exocrafts and "Set as current"
* Renaming for Storage Container
* Buttons to select the previous/next inventory with a single click
* Buttons to enable/repair/fill all slots at once

### Changed
* Moved content of **Discoveries** tab to new **Knowledge** tab
* Changed legacy colors for living ships to be only available in debug mode
* Improved visuals to be even closer to the game:
    * Indication for enforced items and those who cannot be deleted in game
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
  a save and it is the active Exocraft

### Fixed
* Not updating "Ships Destroyed" milestone when changing its separated values
* A bunch of data type mismatches and other mapping issues in the (auto-generated)
  save file objects that [could corrupt a save](https://www.reddit.com/r/NoMansSkyMods/comments/g4e3zv/new_savegame_editor/fo60ja1/)

## 2.2.0.0-alpha.2 (2020-04-19)
![Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/2.2.0.0-alpha.2/total)

### Added
* Logging
* **Milestone** tab with all milestones you see in game

## 2.2.0.0-alpha.1 (2020-04-12)

* First public pre-release
