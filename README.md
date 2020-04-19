<!--<a href="https://github.com/cengelha/NomNom/releases/latest/download/NomNom.zip">
    <img src="https://img.shields.io/badge/dynamic/json.svg?label=download&url=https://api.github.com/repos/NomNom/NMSCoordinates/releases/latest&query=$.assets[0].name&style=for-the-badge" alt="Download"/>
</a>-->

# NomNom

<span style="color: red;">__Currently in early development.__ All features are
tested but mistakes can happen, so be aware of that and backup your saves! As
this README is designed for the final product, have a look at the
[FEATURES](FEATURES.md) file if you want to know what's already implemented.
</span>

<span style="color: orange;">UI is not final and will be cleaned up later. If
you encountered any bugs or when you think something doesn't work as expected
or could be improved (beside the UI and the things in the [ROADMAP](ROADMAP.md))
, let me know with as much information as possible.
</span>

Source code will be available with the first stable release.

## Introduction

NomNom is a savegame editor for __No Man's Sky__, but also shows you a lot of
additional information about the data you're about to change. You can also
easily look up each item individually to examine its attributes, independently
of a savegame, or get other useful information that are not related to a
specific savegame (but enhanced if one is loaded).

If you known the
[NMSSE by goatfungus](https://github.com/goatfungus/NMSSaveEditor) you will
most certainly notice the similarity but there are things missing that I'd like
to have or just not implemented as I like to have it. I also wanted to have a
place where I can directly see how good my stats are, without searching through
an online wiki or such. Therefore I started my own project for fun and here we
are.

## Features

The features can divided into 5 main parts:
* __Manager__ Manage your saves!
  * Automatic backup and recovery (in case you screw something up).
  * Copy a save to another slot.
  * Save your save as human readable JSON.
  * Delete your save.
* __Editor__ Edit your save for your needs!
  * Ability to change data values and organize inventories.
  * Ability to manage your fleet of frigates including expeditions.
  * Ability to customize appearances.
  * Ability to edit your knowledge and recorded experiences.
  * Ability to edit the raw JSON (for advanced users only)!
* __Coordinates__ Travel around the galaxy!
  * Fast travel to any system you like.
  * Trigger space battles.
  * Clear portal interference.
* __Discovery__ Useful tips!
  * What to expect in system with specific races, wealth, etc.
* __Catalogue__ Explore all the items!
  * Just as in-game, look up items and get additional information about it.

A detailed list can be found [here](FEATURES.md) and a list of things to come
[here](ROADMAP.md).

<img src="images/editor_suit.png" width="49%"/> <img src="images/editor_starship.png" width="49%"/>
<img src="images/editor_frigate.png" width="49%"/> <img src="images/editor_base.png" width="49%"/>

The images are from version
[2.2.0.0-alpha.2](https://github.com/cengelha/NomNom/releases/tag/2.2.0.0-alpha.2)
. More can be found [here](images).

## Getting Started

### Requirements

* The newest version of NomNom is built for __No Man's Sky Synthesis (2.2)__.
  If you use it with a game version branch below (e.g. __Beyond 2.0__) or above
  (e.g. __2.3__), things may not work correctly.
* You need .NET Framework 4.7.2.
  * It's included in the Windows 10 April 2018 Update and above.
  * Otherwise you can download it
    [here](http://go.microsoft.com/fwlink/?LinkId=863262).

### Instructions

1. As the tool includes an automatic backup functionality you don't need to do
   it manually but if you want to be absolutely save, do it.
1. You may want to create a shortcut to the executable for easier access.
1. At first start the tools tries to locate your savegames at the default
   location but if that fails, you have to select it manually.
1. Select a slot.
1. Start tinkering!

## Notes

* Restrictions that are enforced by the game, even if you changed it manually
  will not be possible to disable. If you can't do something, that's probably
  the reason why.
* Items _"Foundation Strut"_ and _"Foundation Strut Quad"_ are not listed as
  they cannot be used in-game even though they are unlockable in the Nexus.

## Versioning

The versioning is oriented on the game version itself:

* _Major_ mirrors the games major version.
* _Minor_ represents big, named updates and mirrors their initial minor version
  (e.g. NEXT 1.5 or Synthesis 2.2).
* _Patch_ includes new features, bug fixes, updated game assets an such beside
  the named game updates.

## Changelog

The complete history can be found in the [CHANGELOG](CHANGELOG.md) file.

## Authors

* __Christian Engelhardt__ - [GitHub](https://github.com/cengelha) - [Reddit](https://www.reddit.com/user/zencq)

## License

This project is licensed under the GNU GPLv3 license - see the
[LICENSE](LICENSE) file for details.

## Credits

* [goatfungus](https://github.com/goatfungus/NMSSaveEditor)
* [hbouma](https://github.com/goatfungus/NMSSaveEditor/issues/158)
* [jeffswt](https://github.com/goatfungus/NMSSaveEditor/issues/200)
* [Kevin0M16](https://github.com/Kevin0M16/NMSCoordinates)
* [matthew-humphrey](https://github.com/matthew-humphrey/nmssavetool)
* [u/_lmonk](https://www.reddit.com/r/NoMansSkyMods/comments/dkob5c/manual_ship_and_multitool_color_customization/)
* [u/Artimec_w](https://www.reddit.com/r/NoMansSkyMods/comments/6fr5td/tutorial_convert_signal_booster_coordinates_to/)
