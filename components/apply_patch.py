import os
import sys
from components import gui_popup
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))

def APPLY_PATCH(SETTINGS_PATH, PATCH_PATH):
    PATCH_PATH = os.path.join(BASE_DIR, PATCH_PATH)
    PATCH_PATH = Path(PATCH_PATH)
    COPIED_FILES = [] # list of files copied. 

    for src in PATCH_PATH.iterdir():

        dst = Path(SETTINGS_PATH) / src.name # destination path
        if dst.exists() and not dst.stat().st_mode & 0o200:
            dst.chmod(0o666) # remove read only
        dst.write_bytes(src.read_bytes())
        dst.chmod(0o444) # put back read only
        COPIED_FILES.append(src.name)

    gui_popup.show_popup(COPIED_FILES, SETTINGS_PATH)

def APPLY_POTATO(SETTINGS_PATH):
    PATCH_PATH = "setting_files/Potato/"
    APPLY_PATCH(SETTINGS_PATH, PATCH_PATH)


def APPLY_LOW(SETTINGS_PATH):
    PATCH_PATH = "setting_files/Low/"
    APPLY_PATCH(SETTINGS_PATH, PATCH_PATH)


def APPLY_MEDIUM(SETTINGS_PATH):
    PATCH_PATH = "setting_files/Medium/"
    APPLY_PATCH(SETTINGS_PATH, PATCH_PATH)


def APPLY_DEFAULT(SETTINGS_PATH):
    PATCH_PATH = "setting_files/Default/"
    APPLY_PATCH(SETTINGS_PATH, PATCH_PATH)