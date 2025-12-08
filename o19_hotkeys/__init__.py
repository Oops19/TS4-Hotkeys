#
# LICENSE None / You are allowed to use this mod in TS4
# © 2025 https://github.com/Oops19
#


import builtins
from functools import wraps
import sys

if sys.platform == 'darwin':
    # Save the original import function
    _original_import = builtins.__import__

    @wraps(_original_import)
    def filtered_import(name, globals=None, locals=None, fromlist=(), level=0):
        if 'o19_hotkeys' in name:
            return None  # Silently skip loading
        return _original_import(name, globals, locals, fromlist, level)

    # Inject the filtered import logic
    builtins.__import__ = filtered_import
