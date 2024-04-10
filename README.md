# NomNom

![Maintained](https://img.shields.io/maintenance/yes/2024)
[![Release](https://img.shields.io/github/v/release/zencq/NomNom?include_prereleases&display_name=tag)](https://github.com/zencq/nomnom/releases/latest)
[![Release Date](https://img.shields.io/github/release-date-pre/zencq/nomnom)](https://github.com/zencq/nomnom/releases/latest)
![Downloads](https://img.shields.io/github/downloads/zencq/nomnom/total)

[![Platform](https://img.shields.io/badge/platform-windows-lightgrey)](https://www.microsoft.com/en-us/windows)
[![.NET 6](https://img.shields.io/badge/.NET-6-lightgrey)](https://dotnet.microsoft.com/en-us/)
[![C# 10](https://img.shields.io/badge/C%23-10-lightgrey)](https://docs.microsoft.com/en-us/dotnet/csharp/)

[![Discord Server](https://img.shields.io/discord/762409407488720918?color=5865F2&label=discord)](https://discord.gg/3VrAhJVGn7)
[![Supported by the No Man's Sky Community Developers & Designers](https://raw.githubusercontent.com/NMSCD/About/master/badge/purple.svg)](https://nmscd.com/)

[![Donate via Buy Me a Coffee](https://img.shields.io/badge/donate-Buy%20Me%20a%20Coffee-FFDD00)](https://www.buymeacoffee.com/cengelha)
[![Donate via GitHub Sponsors](https://img.shields.io/badge/donate-GitHub%20Sponsors-EA4AAA)](https://github.com/sponsors/cengelha)
[![Donate via Ko-fi](https://img.shields.io/badge/donate-Ko--fi-%23FF5E5B)](https://ko-fi.com/cengelha)
[![Donate via Patreon](https://img.shields.io/badge/donate-Patreon-FF424D)](https://www.patreon.com/cengelha)
[![Donate via PayPal](https://img.shields.io/badge/donate-PayPal-00457C)](https://www.paypal.me/cengelha)

### Table of Contents
- [NomNom](#nomnom)
    - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [State of Development](#state-of-development)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Compatibility](#compatibility)
    - [Requirements](#requirements)
    - [Download](#download)
    - [Instructions](#instructions)
      - [GUI](#gui)
  - [Versioning](#versioning)
  - [Changelog](#changelog)
  - [License](#license)
  - [Contact \& Support](#contact--support)
  - [Authors](#authors)
  - [Credits](#credits)
  - [Dependencies](#dependencies)

## Introduction

NomNom is a savegame editor for **[No Man's Sky](https://www.nomanssky.com/)**,
but also shows you additional information around the data you are about to change.
You can also easily look up each item individually to examine its attributes,
independently of a savegame, or get other useful information that are not related
to a specific one (but enhanced if one is loaded).

You will most certainly notice a similarity to the editor by [goatfungus](https://github.com/goatfungus)
but when this project started it was the only one working and the general layout
was good, so why reinventing the wheel? But there are features missing I would like
to have and (in my eyes) bad usability in some areas. I also wanted to have a place
where I can directly see how good my stats are, without searching through an online
wiki or such. Therefore I started my own project for fun and here we are.

## Features

The features of NomNom can be divided into the different main parts you will see
below. A detailed list can be found in the [FEATURES](FEATURES.md) file.
* __Manager__ Manage your saves!
    * Automatic backup and recovery (in case you screw something up).
    * Save your save as human-readable JSON.
    * Copy, move, and swap slots to another.
    * Transfer your save to another platform you own the game on.
    * Delete your save.
* __Editor__ Edit your save for your needs!
    * Ability to edit cross-save rewards from Expeditions, Twitch Drops, Titles
      and more.
    * Ability to manage fleets, change data values like currencies and stats,
      and organize inventories.
    * Ability to fast travel to any system you like and trigger space battles.
    * Ability to customize appearances.
    * Ability to edit your knowledge and recorded experiences.
    * Ability to edit the raw JSON (for advanced users).
<!-- * __Guide__ Useful tips!
    * What to expect in systems with specific races, wealth, etc.
* __Catalogue__ Explore all the items!
    * Just as in game, look up items and get additional information about it. -->

[<img alt="Manager" src=".github/images/manager.png" width="49.68%"/>](https://raw.githubusercontent.com/cengelha/NomNom/4.00.0.31-beta.1/.github/images/manager.png) [<img alt="Starship" src=".github/images/editor_starship.png" width="49.68%"/>](https://raw.githubusercontent.com/cengelha/NomNom/4.00.0.31-beta.1/.github/images/editor_starship.png)
[<img alt="Manage Fleet" src=".github/images/editor_frigate.png" width="49.68%"/>](https://raw.githubusercontent.com/cengelha/NomNom/4.00.0.31-beta.1/.github/images/editor_frigate.png) [<img alt="Base" src=".github/images/editor_base.png" width="49.68%"/>](https://raw.githubusercontent.com/cengelha/NomNom/4.00.0.31-beta.1/.github/images/editor_base.png)

The images are from version
[4.00.0.31-beta.1](CHANGELOG.md#400031-beta1-2022-10-31).
More and maybe newer can be found [here](https://github.com/cengelha/NomNom/tree/master/.github/images).

## Getting Started

### Compatibility

The latest version of NomNom is built with **Omega 4.50**
in mind. Previous versions are compatible with **Beyond 2.11** and up. If you use it with a game
version branch above (e.g. **5.00**), things should work as usual in most cases
but there can always be a breaking change.

Each version is properly supported with its own set of available items and features.

Each platform has anchor file patterns to check whether it is worth to look further
into the selected directory. This must be in or one level below the selected one.

* [GOG.com](https://www.gog.com/game/no_mans_sky) (Windows PC)
    * Location: **%AppData%\HelloGames\NMS\DefaultUser**
    * File Patterns: **save\*.hg**
* [PlayStation 4](https://store.playstation.com/?resolve=EP2034-CUSA03952_00-NOMANSSKYHG00001)
    * File Patterns: **memory.dat**, **savedata\*.hg**
    * Notes: There are a few options to do this. The only one that does not require
      homebrew is [SaveWizard](https://www.savewizard.net). Two other tools that
      are confirmed working are [Save Mounter](https://github.com/ChendoChap/Playstation-4-Save-Mounter)
      and [Apollo](https://github.com/bucanero/apollo-ps4) but require homebrew.
      Results of other tools may or may not work but the code is as generic as possible.
* [PlayStation 5](https://store.playstation.com/?resolve=EP2034-CUSA03952_00-NOMANSSKYHG00001)
    * Notes: This version of the game is not supported due to restrictions on the
      console itself. By playing the PlayStation 4 version on it, you can still
      save edit with [a few additional steps](https://docs.google.com/document/d/1QoD2-PNlX-HeR5K1zuPGLMLBcX4_wknkhzc43-9bEq4/edit?usp=sharing).
* [Steam](https://store.steampowered.com/app/275850/No_Mans_Sky/) (PC)
    * Location
      * Windows: **%AppData%\HelloGames\NMS\st\_\<SteamID\>**
      * SteamDeck: **~/.local/share/Steam/steamapps/compatdata/275850/pfx/drive_c/users/steamuser/Application Data/HelloGames/NMS/st\_\<SteamID\>**
      * macOS: **~/Library/Application Support/HelloGames/NMS/st\_\<SteamID\>**
    * File Patterns: **save\*.hg**
* [Microsoft Store](https://www.microsoft.com/p/no-mans-sky/bqvqtl3pch05) (Windows PC)
    * Location: **%LocalAppData%\Packages\HelloGames.NoMansSky_bs190hzg1sesy\SystemAppData\wgs\\<XboxID\>_29070100B936489ABCE8B9AF3980429C**
    * File Patterns: **containers.index**
    * Notes: Reloading of modified saves while the game is running does not work.
* [Nintendo Switch](https://www.nintendo.com/store/products/no-mans-sky-switch)
    * File Patterns: **manifest\*.dat**
    * Notes: To get your saves you need homebrew software on your Switch. [EdiZon](https://github.com/WerWolv/EdiZon)
      and [JKSV](https://github.com/J-D-K/JKSV) are confirmed working. Results of
      other tools may or may not work but the code is as generic as possible.
* [Xbox One/Series X\|S](https://www.microsoft.com/p/no-mans-sky/bqvqtl3pch05)
    * Notes: Not directly supported but can easily achieved with cloud sync via
      the Microsoft Store. The synchronization is triggered short after you close
      the game (no need to load a save).

### Requirements

<!-- If just want to use NomNom without bothering youself about dependencies, you can
just use the self-contained variant. It contains the required .NET runtime but has
an increased file size and may need longer to start.

If you are fine with installing the required .NET runtime, you just need to install
the **[.NET 6 Desktop Runtime](https://dotnet.microsoft.com/download/dotnet/6.0)**
and that is it. -->

You just need to install the **[.NET 6 Desktop Runtime](https://dotnet.microsoft.com/download/dotnet/6.0)**
and that is it.

### Download

* [GitHub](https://github.com/cengelha/NomNom/releases) (NomNom.zip)
* [Nexus Mods](https://www.nexusmods.com/nomanssky/mods/1566?tab=files)

### Instructions

#### GUI

1. After downloading and extracting the zip file you'll find a few files. All
   you need to care about is the executable (`NomNom.exe`) but new folders may
   be created at runtime (e.g. for backups) that will become relevant to you.
1. You may want to create a shortcut to the executable for easier access.
1. As the tool includes an automatic backup functionality you don't need to do
   it manually but if you want to be absolutely save, do it.
1. At first start the tools locates your saves at the default
   location of each platform but if that fails, you have to select it manually.
1. Select a slot.
1. Start tinkering!
1. Guide and Catalogue will work without loading a save.

<!-- #### CLI

... -->

## Versioning

The versioning is oriented on the game version itself:

* _Major_ mirrors the games major version.
* _Minor_ mirrors the games initial minor version of named updates
  (e.g. **Synthesis 2.20** or **Outlaws 3.85**).
* _Patch_ includes new features, bug fixes, updated game assets, and such beside
  the named game updates.
* _Revision_ serves as public release counter.

## Changelog

The complete history can be found in the [CHANGELOG](CHANGELOG.md) file.

There is also a [ROADMAP](ROADMAP.md) file with things planned for the future. It's
not set in stone but you will get an idea what is coming next.

## License

This project is licensed under the GNU GPLv3 license - see the [LICENSE](LICENSE)
file for details.

## Contact & Support

If you like NomNom and want to support me in its further development, you can do
so here on [__GitHub__](https://github.com/sponsors/cengelha), on [__Buy Me a Coffee__](https://www.buymeacoffee.com/cengelha), [__Ko-fi__](https://ko-fi.com/cengelha), or [__Patreon__](https://www.patreon.com/cengelha) or via [__PayPal__](https://www.paypal.me/cengelha).
I will appreciate it!

The official [__Discord__](https://discord.gg/3VrAhJVGn7) server will be the
place where you will find all information at one place, first hand. If you need
(or want to offer) help, found a bug, have a suggestion, or something else
regarding NomNom, you will find, or can post it there.

## Authors

* **Christian Engelhardt** (zencq) - [GitHub](https://github.com/cengelha) - [Nexus Mods](https://www.nexusmods.com/nomanssky/users/73645048) - [Reddit](https://www.reddit.com/user/zencq)

## Credits

Thanks to the following people for their help in one way or another.

* [goatfungus](https://github.com/goatfungus/NMSSaveEditor) - Inspiration and verifying my own implementation
* [hbouma](https://github.com/goatfungus/NMSSaveEditor/issues/158) - Explaining how clearing TerrainEdit works
* [jeffswt](https://github.com/goatfungus/NMSSaveEditor/issues/200) - Algorithm to properly move base computer
* [jaszhix](https://github.com/jaszhix/NoMansConnect) - [rogerhnn](https://github.com/nmsportals/nmsportals.github.io) - Coordinate conversion
* [KhaozTopsy](https://api.nmsassistant.com) - Creating the Assistant for No Man's Sky API to get live data and make the transfer to the app possible
* [Novoca1n3](https://discord.gg/3VrAhJVGn7) - Providing a proof-of-concent for the JSON editor with tree view
* [zousug](https://discord.gg/3VrAhJVGn7) - Helping to set up the Discord server

And not to forget those whose help contributed to parts of the outsourced libraries
[libNOM.collect](https://github.com/zencq/libNOM.collect#credits), [libNOM.io](https://github.com/zencq/libNOM.io#credits), and [libNOM.map](https://github.com/zencq/libNOM.map#credits).

## Dependencies

* [CsvHelper](https://www.nuget.org/packages/CsvHelper/) - reading CSV files from [Pi](https://github.com/zencq/Pi)
* [Humanizer.Core](https://www.nuget.org/packages/Humanizer.Core/) - manipulating and displaying strings, enums, and more
* [LazyCache](https://www.nuget.org/packages/LazyCache/) - in-memory caching
* [libNOM.collect](https://github.com/zencq/libNOM.collect) - backup and restore collections
* [libNOM.io](https://github.com/zencq/libNOM.io) - read and write save files as well as related actions
* [libNOM.map](https://github.com/zencq/libNOM.map) - obfuscate and deobfuscate save files
* [Newtonsoft.Json](https://www.nuget.org/packages/Newtonsoft.Json/) - high-performance JSON framework
* [Octokit](https://www.nuget.org/packages/Octokit/) - GitHub API
* [Pfim](https://www.nuget.org/packages/Pfim/) - image decoder for direct draw surface (.dds) images
* [RestSharp](https://www.nuget.org/packages/RestSharp/) - generic REST API
* [Unleash.Client](https://www.nuget.org/packages/Unleash.Client/) - feature toggles

<!-- * [Autoupdater.NET.Official](https://www.nuget.org/packages/Autoupdater.NET.Official/) - auto update functionality
* [Autoupdater.NET.Official](https://www.nuget.org/packages/Autoupdater.NET.Official/) - auto update functionality
* [Autoupdater.NET.Official](https://www.nuget.org/packages/Autoupdater.NET.Official/) - auto update functionality
* [Autoupdater.NET.Official](https://www.nuget.org/packages/Autoupdater.NET.Official/) - auto update functionality -->
