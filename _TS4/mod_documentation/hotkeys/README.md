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


# 📝 Addendum

## 🔄 Game compatibility
This mod has been tested with `The Sims 4` 1.119.109, S4CL 3.15, TS4Lib 0.3.42.
It is expected to remain compatible with future releases of TS4, S4CL, and TS4Lib.

## 📦 Dependencies
Download the ZIP file - not the source code.
Required components:
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not already installed, download and install TS4 and the listed mods. All are available for free.

## 📥 Installation
* Locate the localized `The Sims 4` folder (it contains the `Mods` folder).
* Extract the ZIP file directly into this folder.

This will create:
* `Mods/_o19_/$mod_name.ts4script`
* `Mods/_o19_/$mod_name.package`
* `mod_data/$mod_name/*`
* `mod_documentation/$mod_name/*` (optional)
* `mod_sources/$mod_name/*` (optional)

Additional notes:
* CAS and Build/Buy UGC without scripts will create `Mods/o19/$mod_name.package`.
* A log file `mod_logs/$mod_name.txt` will be created once data is logged.
* You may safely delete `mod_documentation/` and `mod_sources/` folders if not needed.

### 📂 Manual Installation
If you prefer not to extract directly into `The Sims 4`, you can extract to a temporary location and copy files manually:
* Copy `mod_data/` contents to `The Sims 4/mod_data/` (usually required).
* `mod_documentation/` is for reference only — not required.
* `mod_sources/` is not needed to run the mod.
* `.ts4script` files can be placed in a folder inside `Mods/`, but storing them in `_o19_` is recommended for clarity.
* `.package` files can be placed in a anywhere inside `Mods/`.

## 🛠️ Troubleshooting
If installed correctly, no troubleshooting should be necessary.
For manual installs, verify the following:
* Does your localized `The Sims 4` folder exist? (e.g. localized to Die Sims 4, Les Sims 4, Los Sims 4, The Sims 4, ...)
  * Does it contain a `Mods/` folder?
    * Does Mods/_o19_/ contain:
      * `ts4lib.ts4script` and `ts4lib.package`?
      * `{mod_name}.ts4script` and/or `{mod_name}.package`
* Does `mod_data/` contain `{mod_name}/` with files?
* Does `mod_logs/` contain:
  * `Sims4CommunityLib_*_Messages.txt`?
  * `TS4-Library_*_Messages.txt`?
  * `{mod_name}_*_Messages.txt`?
* Are there any `last_exception.txt` or `last_exception*.txt` files in `The Sims 4`?


* When installed properly this is not necessary at all.
For manual installations check these things and make sure each question can be answered with 'yes'.
* Does 'The Sims 4' (localized to Die Sims 4, Les Sims 4, Los Sims 4, The Sims 4, ...) exist?
  * Does `The Sims 4` contain the folder `Mods`?
    * Does `Mods` contain the folder `_o19_`? 
      * Does `_19_` contain `ts4lib.ts4script` and `ts4lib.package` files?
      * Does `_19_` contain `{mod_name}.ts4script` and/or `{mod_name}.package` files?
  * Does `The Sims 4` contain the folder `mod_data`?
    * Does `mod_data` contain the folder `{mod_name}`?
      * Does `{mod_name}` contain files or folders?
  * Does `The Sims 4` contain the `mod_logs` ?
    * Does `mod_logs` contain the file `Sims4CommunityLib_*_Messages.txt`?
    * Does `mod_logs` contain the file `TS4-Library_*_Messages.txt`?
      * Is this the most recent version or can it be updated?
    * Does `mod_logs` contain the file `{mod_name}_*_Messages.txt`?
      * Is this the most recent version or can it be updated?
  * Doesn't `The Sims 4` contain the file(s) `last_exception.txt`  and/or `last_exception*.txt` ?
* Share the `The Sims 4/mod_logs/Sims4CommunityLib_*_Messages.txt` and `The Sims 4/mod_logs/{mod_name}_*_Messages.txt`  file.

If issues persist, share:
`mod_logs/Sims4CommunityLib_*_Messages.txt`
`mod_logs/{mod_name}_*_Messages.txt`

## 🕵️ Usage Tracking / Privacy
This mod does not send any data to external servers.
The code is open source, unobfuscated, and fully reviewable.

Note: Some log entries (especially warnings or errors) may include your local username if file paths are involved.
Share such logs with care.

## 🔗 External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## ⚖️ Copyright and License
* © 2020-2025 [Oops19](https://github.com/Oops19)
* `.package` files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* All other content (unless otherwise noted): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 

You may use and adapt this mod and its code — even without owning The Sims 4.
Have fun extending or integrating it into your own mods!

Oops19 / o19 is not affiliated with or endorsed by Electronic Arts or its licensors.
Game content and materials © Electronic Arts Inc. and its licensors.
All trademarks are the property of their respective owners.

## 🧾 Terms of Service
* Do not place this mod behind a paywall.
* Avoid creating mods that break with every TS4 update.
* For simple tuning mods, consider using:
  * [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
  * [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To verify custom tuning structures, use:
  * [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).

## 🗑️ Removing the Mod
Installing this mod creates files in several directories. To fully remove it, delete:
* `The Sims 4/Mods/_o19_/$mod_name.*`
* `The Sims 4/mod_data/_o19_/$mod_name/`
* `The Sims 4/mod_documentation/_o19_/$mod_name/`
* `The Sims 4/mod_sources/_o19_/$mod_name/`

To remove all of my mods, delete the following folders:
* `The Sims 4/Mods/_o19_/`
* `The Sims 4/mod_data/_o19_/`
* `The Sims 4/mod_documentation/_o19_/`
* `The Sims 4/mod_sources/_o19_/`
