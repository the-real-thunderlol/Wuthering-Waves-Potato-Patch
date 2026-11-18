import os

def APPLY_PATCH(SETTINGS_PATH, PATCH_PATH):
    PATCH_PATH = os.path.dirname(__file__) + "\\" + PATCH_PATH

    PATCH_PATH = PATCH_PATH.replace("/", "\\")
    SETTINGS_PATH = SETTINGS_PATH.replace("/", "\\")

    os.system(f'copy /Y "{PATCH_PATH}*" "{SETTINGS_PATH}"')

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
