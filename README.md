# NomNom

<span style="color: red;">__Currently in a pre-release state.__ All available
features are tested while implemented but mistakes can happen, so be aware of
that and backup your saves!</span>

<span style="color: orange;">As this README is designed for the final product,
have a look at the [FEATURES](FEATURES.md) file if you want to know what's
already implemented. Currently not all planned features are already implemented
but most of what goatfungus' editor can (and more) is already there.</span>

<span style="color: orange;">Things may be a little buggy and the UI is
definitely not final. NomNom stays in alpha until it's feature complete and beta
is about code and UI cleanup/polishing and fixing the remaining bugs. If you
encountered any bugs or when you think something doesn't work as expected
or could be improved (beside the things in the [ROADMAP](ROADMAP.md)), let me
know with as much information as possible.</span>

**Source code will be available with the first stable release.**

![Maintained](https://img.shields.io/maintenance/yes/2020)
[![Support Patreon](https://img.shields.io/badge/support-Patreon-brightgreen)](https://www.patreon.com/cengelha)
[![Support PayPal](https://img.shields.io/badge/support-PayPal-brightgreen)](https://www.paypal.me/cengelha)
![Release Downloads](https://img.shields.io/github/downloads/cengelha/nomnom/total)

<!-- ![Release](https://img.shields.io/github/v/release/cengelha/nomnom)
![Release Date](https://img.shields.io/github/release-date/cengelha/nomnom) -->

![Pre-release](https://img.shields.io/github/v/release/cengelha/nomnom?include_prereleases)
![Pre-release Date](https://img.shields.io/github/release-date-pre/cengelha/nomnom)

## Introduction

NomNom is a savegame editor for [__No Man's Sky__](https://www.nomanssky.com/),
but also shows you a lot of additional information around the data you're about
to change. You can also easily look up each item individually to examine its
attributes, independently of a savegame, or get other useful information that
are not related to a specific savegame (but enhanced if one is loaded).

If you known the [NMSSE by goatfungus](https://github.com/goatfungus/NMSSaveEditor)
you will most certainly notice the similarity but his tool has features missing
that I'd like to have and (in my eyes) bad usability in some areas. I also
wanted to have a place where I can directly see how good my stats are, without
searching through an online wiki or such. Therefore I started my own project for
fun and here we are.

If you're interested in some technical insights in general, you can get some in
the [NMS Community Developers & Designers](https://nmscd.github.io/) DevTalks
that I join regularly.

There is a [Patreon page](https://www.patreon.com/cengelha) in case you want to
support me (no paywall), but I will also use it as developer diary to keep you
updated.

## Features

The features can divided into different main parts:
* __Manager__ Manage your saves!
    * Automatic backup and recovery (in case you screw something up).
    * Save your save as human-readable JSON.
    * Copy or move a save to another slot.
    * Delete your save.
* __Editor__ Edit your save for your needs!
    * Ability to manage fleets, change data values, and organize inventories.
    * Ability to fast travel to any system you like, trigger space battles, and
      clear portal interference.
    * Ability to customize appearances.
    * Ability to edit your knowledge and recorded experiences.
    * Ability to edit the raw JSON (for advanced users only).
* __Guide__ Useful tips!
    * What to expect in systems with specific races, wealth, etc.
* __Catalogue__ Explore all the items!
    * Just as in-game, look up items and get additional information about it.

A detailed list can be found [here](FEATURES.md) and a list of things to come
[here](ROADMAP.md).

[<img alt="Exosuit" src="images/editor_suit.png" width="49.68%"/>](https://raw.githubusercontent.com/cengelha/NomNom/master/images/editor_suit.png) [<img alt="Starship" src="images/editor_starship.png" width="49.68%"/>](https://raw.githubusercontent.com/cengelha/NomNom/master/images/editor_starship.png)
[<img alt="Frigate" src="images/editor_frigate.png" width="49.68%"/>](https://raw.githubusercontent.com/cengelha/NomNom/master/images/editor_frigate.png) [<img alt="Base" src="images/editor_base.png" width="49.68%"/>](https://raw.githubusercontent.com/cengelha/NomNom/master/images/editor_base.png)

The images are from version
[2.2.0.0-alpha.2](https://github.com/cengelha/NomNom/releases/tag/2.2.0.0-alpha.2).
More can be found [here](https://github.com/cengelha/NomNom/tree/master/images).

## Getting Started

### Requirements

* NomNom is compatible with the following platforms of the game:
  Platform                                                                                   | Detect                  | Read                    | Write                   | File Pattern    | Note
  ------------------------------------------------------------------------------------------ | :---------------------: | :---------------------: | :---------------------: | --------------- | ----
  [GOG.com](https://www.gog.com/game/no_mans_sky) (PC)                                       | <ul><li> [X] </li></ul> | <ul><li> [X] </li></ul> | <ul><li> [X] </li></ul> | save*.hg        | Same file format as Steam. Even though everything in NomNom is labeled with Steam, you can still use it for GOG.com without restrictions.
  [PlayStation](https://store.playstation.com/?resolve=EP2034-CUSA03952_00-NOMANSSKYHG00001) | <ul><li> [X] </li></ul> | <ul><li> [X] </li></ul> | <ul><li> [X] </li></ul> | memory.dat      | Tested with [SaveWizard](https://www.savewizard.net/) dumps. Results of other tools will probably not work.
  [Steam](https://store.steampowered.com/app/275850/No_Mans_Sky/) (PC)                       | <ul><li> [X] </li></ul> | <ul><li> [X] </li></ul> | <ul><li> [X] </li></ul> | save*.hg        |
  [Windows Store](https://www.microsoft.com/p/no-mans-sky/bqvqtl3pch05) (PC)                 | <ul><li> [ ] </li></ul> | <ul><li> [ ] </li></ul> | <ul><li> [ ] </li></ul> | container.index | Pending. Will be added in alpha.7
  Xbox                                                                                       | <ul><li> [ ] </li></ul> | <ul><li> [ ] </li></ul> | <ul><li> [ ] </li></ul> |                 |

  Each platform has a anchor file pattern to check whether it's worth to search
  a directory or not. This must be in or one directory below the selected one.
* The latest version of NomNom is built with __Exo Mech/Crossplay (2.4-2.5)__ in
  mind but is compatible with __Synthesis (2.2)__ and up. If you use it with a game
  version branch above (e.g. __3.0__), things should work as usual in most cases
  but there can always be breaking changes. Watch out for notices about new
  game updates on the [Patreon page](https://www.patreon.com/cengelha).
* You need .NET Framework 4.8.
    * It's included in the Windows 10 May 2019 Update (1903) and above.
    * Otherwise you can download it [here](https://dotnet.microsoft.com/download/dotnet-framework/net48).

### Instructions

1. You may want to create a shortcut to the executable for easier access.
1. As the tool includes an automatic backup functionality you don't need to do
   it manually but if you want to be absolutely save, do it.
1. At first start the tools tries to locate your saves at the default
   location of each platform but if that fails, you have to select it manually.
1. Select a slot.
1. Start tinkering!
1. Guide and Catalogue will work without loading a save.

## Notes

* Restrictions that are enforced by the game, even if you changed it manually
  will not be possible to disable. If you can't do something, that's probably
  the reason why.

## Versioning

The versioning is oriented on the game version itself:

* _Major_ mirrors the games major version.
* _Minor_ mirrors the games initial minor version of named updates
  (e.g. NEXT 1.5 or Synthesis 2.2).
* _Patch_ includes new features, bug fixes, updated game assets, and such beside
  the named game updates.
* _Revision_ serves as public release counter.

## Changelog

The complete history can be found in the [CHANGELOG](CHANGELOG.md) file.

## License

This project is licensed under the GNU GPLv3 license - see the
[LICENSE](LICENSE) file for details.

## Authors

* __Christian Engelhardt__ - [GitHub](https://github.com/cengelha) - [Nexus Mods](https://www.nexusmods.com/nomanssky/users/73645048) - [Patreon](https://www.patreon.com/cengelha) - [Reddit](https://www.reddit.com/user/zencq)

## Credits

* [goatfungus](https://github.com/goatfungus/NMSSaveEditor) - [Kevin0M16](https://github.com/Kevin0M16) - Inspiration and verifying my own implementation
* [hbouma](https://github.com/goatfungus/NMSSaveEditor/issues/158) - Explaining how clearing TerrainEdit works
* [jaszhix](https://github.com/jaszhix/NoMansConnect) - [rogerhnn](https://github.com/nmsportals/nmsportals.github.io) - Coordinate conversion
* [jeffswt](https://github.com/goatfungus/NMSSaveEditor/issues/200) - Algorithm for proper base computer moving
* [matthew-humphrey](https://github.com/matthew-humphrey/nmssavetool) - Decrypt and encrypt Steam saves
* [monkeyman192](https://github.com/monkeyman192/MBINCompiler) - MBINCompiler to extract data from the game files
* [u/_lmonk](https://www.reddit.com/r/NoMansSkyMods/comments/dkob5c/manual_ship_and_multitool_color_customization/) - Explaining how color customization for Starship and Multi-Tool works
* [u/MegaGold_Fighter](https://www.reddit.com/r/NoMansSkyMods/comments/hhe2he/ps4_nms_save_editing_general_guide/) - Providing valuable data to make the PlayStation support possible
* [Moo#6953](https://discord.com/) - Helping and verifying the Windows Store encryption
