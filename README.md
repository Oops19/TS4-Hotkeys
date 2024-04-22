# TS4 Hotkeys & Gamepad

This mod is for Windows only and does not work on any other systems.

## Hotkeys
This mod allows to define custom hotkeys for the keyboard keys [A-Z0-9].
It supports Shift, Ctrl, Alt and/or Win key modifiers.
The mod itself doesn't come with any pre-defined hotkey definitions.

## Gamepad
The mod supports using the gamepad to move sims around.
The support to route sims to a location is very basic and may throw exceptions.
Custom actions can't be bound to the gamepad keys, except of the paddle key which always act as normal keys. 
* The left stick can be used to rotate the sim.
* The left shoulder key activates the trigger keys to rotate the sim around the Y axis.
* The right stick can be used to move the sim.
* The right shoulder key activates the trigger keys to move the sim up/down (Y axis).
* The DPAD can be used to send the sim into the corresponding location. This may fail and/or throw exceptions. Please do not report any exceptions thrown while using the DPAD.
* The ABXY, menu and play keys are not yet used.
* The game key can't be used.

### Cheats
* o19.hk.gp.id ID - Select the controller ID (0-3) to be used. Defaults to the fist controller '0'.
* o19.hk.gp.verbose - Write a verbose log. This will cause some lag while using the controller.

### Moving Objects
There is a simple cheat interaction called 'Move'. Running it on the floor allows to move the `active` sim (default).
Clicking on a object/(not controlled) sim allows to move and/or rotate the object/sim.



# Addendum

## Game compatibility
This mod has been tested with `The Sims 4` 1.106.148, S4CL 3.3, TS4Lib 0.2.0 (2024-02).
It is expected to be compatible with many upcoming releases of TS4, S4CL and TS4Lib.

## Dependencies
Download the ZIP file, not the sources.
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not installed download and install TS4 and these mods.
All are available for free.

## Installation
* Locate the localized `The Sims 4` folder which contains the `Mods` folder.
* Extract the ZIP file into this `The Sims 4` folder.
* It will create the directories/files `Mods/_o19_/$mod_name.ts4script`, `Mods/_o19_/$mod_name.package`, `mod_data/$mod_name/*` and/or `mod_documentation/$mod_name/*`
* `mod_logs/$mod_name.txt` will be created as soon as data is logged.

### Manual Installation
If you don't want to extract the ZIP file into `The Sims 4` folder you might want to read this. 
* The files in `ZIP-File/mod_data` are usually required and should be extracted to `The Sims 4/mod_data`.
* The files in `ZIP-File/mod_documentation` are for you to read it. They are not needed to use this mod.
* The `Mods/_o19_/*.ts4script` files can be stored in a random folder within `Mods` or directly in `Mods`. I highly recommend to store it in `_o19_` so you know who created it.

## Usage Tracking / Privacy
This mod does not send any data to tracking servers. The code is open source, not obfuscated, and can be reviewed.

Some log entries in the log file ('mod_logs' folder) may contain the local username, especially if files are not found (WARN, ERROR).

## External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## Copyright and License
* © 2024 [Oops19](https://github.com/Oops19)
* License for '.package' files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* License for other media unless specified differently: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless the Electronic Arts TOS for UGC overrides it.
This allows you to use this mod and re-use the code even if you don't own The Sims 4.
Have fun extending this mod and/or integrating it with your mods.

Oops19 / o19 is not endorsed by or affiliated with Electronic Arts or its licensors.
Game content and materials copyright Electronic Arts Inc. and its licensors. 
Trademarks are the property of their respective owners.

### TOS
* Please don't put it behind a paywall.
* Please don't create mods which break with every TS4 update.
* For simple tuning modifications use [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
* or [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To check the XML structure of custom tunings use [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).
