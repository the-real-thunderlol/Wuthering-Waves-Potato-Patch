import os
import shutil
import sys

BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))

def APPLY_PATCH(SETTINGS_PATH, PATCH_PATH):
    PATCH_PATH = os.path.join(BASE_DIR, PATCH_PATH)

    for name in os.listdir(PATCH_PATH):
        src = os.path.join(PATCH_PATH, name)
        if os.path.isfile(src):
            shutil.copy2(src, SETTINGS_PATH)

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