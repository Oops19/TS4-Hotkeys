# TS4 Hotkeys & Gamepad

This mod is for Windows only and does not work on any other systems.

## Issues
The hotkeys work only while a zone is loaded and the game has the focus.
It is now disabled in CAS but still active in the build/buy menu.
The cheat console and text input in game do lag.
That's because the input can't be processed fast enough due to the limited Python threading capabilities.
Get a much faster processor to fix this.

The gamepad is queried in an active thread around 25 times a second.
This adds some overhead to TS4.
Unplug or disable the gamepad to avoid this in case you don't use it.

Should be solved:
~~There are some issues to detect the focus properly.
In such cases the keys will not work.
Switch to a different window/program and back to TS4 to fix this.~~

## Hotkeys
This mod allows to define custom hotkeys for the keyboard keys [A-Z0-9].
It supports Shift, Ctrl, Alt and/or Win key modifiers.
The mod itself doesn't come with any pre-defined hotkey bindings.

## Gamepad
The mod supports using the gamepad to move sims around in case a 3rd-party mod to move objects/sims is available.
The support to route sims to a location is very basic and may throw exceptions.
Custom actions can't be bound to the gamepad keys, except of the paddle key which always act as normal keys. 
* The left stick can be used to rotate the sim.
* The left shoulder key activates the trigger keys to rotate the sim around the Y axis.
* The right stick can be used to move the sim.
* The right shoulder key activates the trigger keys to move the sim up/down (Y axis).
* The DPAD can be used to send the sim into the corresponding location. This may fail and/or throw exceptions. Please do not report any exceptions thrown while using the DPAD.
* The ABXY, menu and play keys are not yet used.
* The game key can't be used.

### Configuration
The default configuration file is placed in `mod_data/hotkeys/hotkeys.txt` and should not be edited as it will be overridden when updating.
To modify the default values copy it to `mod_data/hotkeys/hotkeys.override.txt` and change values in the new file.
#### Enable / Disable permanently
* To disable the hotkeys permanently change `'Hotkeys': True,` to `'Hotkeys': False,`.
* To disable the gamepad permanently change `'Gamepad': True,` to `'Gamepad': False,`.
* To change the gampepad ID modify `'GamepadId': 0,` to values 1, 2 or 3.

* Other settings should not be modified.

### Cheats
* o19.hk.gp.id ID - Select the controller ID (0-3) to be used. Defaults to the fist controller '0'.
* o19.hk.gp.verbose - Write a verbose log. This will cause some lag while using the controller.

## Pie Menus
### Moving Objects
There is a simple cheat interaction called 'Move'.
* Clicking on a object/(or random) sim allows to move and/or rotate the object/sim. The active sim will be ignored.
* Running it on the floor allows to move the `active` sim (default) again.


# Creation of Custom Hotkey Bindings
Replace directory, author, mod etc. (often mention in `{}` below) with real / useful values. The values and names used when creating a new mod should never contain `{` or `}`.

To add custom hotkeys to the game create a file `The Sims 4/mod_data/hotkeys/hotkeys.{author-name}.{mod-name}.txt` and add hotkey definitions to it. E.g.:
```json
{
  'author-name.mod-name': {
    'A': ['{directory}.{file-name}..{ClassName}.{function_name}', 'Description: A miracle happens.', ],
    'Shift+Ctrl+Alt+Win+A': ['{directory}.{file-name}.{ClassName}.{function_name2} {all parameters}', 'Description: Another miracle happens.', ],
  }
}
```
In case you start TS4 now `Hotkeys` will complain about the missing functions.

Create a mod with the structure from above. It should have a file `{directory}/{file-name}.py` with the following structure:
```python
class {ClassName}:
    @staticmethod
    def {function_name}():
        pass  # code for 'A miracle happens.'
    @staticmethod
    def {function_name2}(*args):
        pass  # code for 'Another miracle happens.'
```

Compile the file to `{directory}/{file-name}.pyc` and add it to a ZIP file with the .ts4script instead of the .zip file suffix.
Add the `{mod-name}.ts4script` file to the mods folder.

Starting TS4 will read the `hotkeys.{author-name}.{mod-name}.txt`, locate the methods in the mod and call it whenever one fo the keys is pressed.


# Addendum

## Game compatibility
This mod has been tested with `The Sims 4` 1.106.148, S4CL 3.3, TS4Lib 0.3.14 (2024-04).
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
