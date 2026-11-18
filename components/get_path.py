import tkinter
from tkinter import filedialog
import os

# first get path
#tkinter popup

def get_path():
    SETTINGS_PATH = check_if_path_exists()

    if SETTINGS_PATH == False:
        EXE_PATH = get_exe_path()
        SETTINGS_PATH = adjust_path(EXE_PATH)

    return SETTINGS_PATH

def update_path():
    EXE_PATH = get_exe_path()
    SETTINGS_PATH = adjust_path(EXE_PATH)

    return SETTINGS_PATH

def check_if_path_exists():
    if not os.path.isfile("config/settings.ini"):
        return False

    with open("config/settings.ini") as file:
        PATH = file.read().split("=", 1)[1].strip()

    if not os.path.isdir(PATH):
        return False

    return PATH


def get_exe_path():
    root = tkinter.Tk()
    root.withdraw()

    EXE_PATH = filedialog.askopenfilename(
        title="Select \"Wuthering Waves\" EXE",
        filetypes=[("Executable files", "*.exe")]
    )

    root.destroy()
    return EXE_PATH

def adjust_path(EXE_PATH):
    # now there are 2 exe paths
    # "Wuthering waves\launcher.exe"
    # "Wuthering Waves\Wuthering Waves Game\Wuthering Waves.exe"

    SETTINGS_PATH = ""
    print(f"Path = {SETTINGS_PATH}\n")

    if   EXE_PATH.endswith("launcher.exe") or EXE_PATH.endswith("uninst.exe"):
        EXE_PATH = os.path.dirname(EXE_PATH)
        SETTINGS_PATH = EXE_PATH + "\Wuthering Waves Game\Client\Saved\Config\WindowsNoEditor"
    elif EXE_PATH.endswith("Wuthering Waves.exe"):
        EXE_PATH = os.path.dirname(EXE_PATH)
        SETTINGS_PATH = EXE_PATH + "\Client\Saved\Config\WindowsNoEditor"
    else:
        print(f"Invalid Path. \nPath recieved: {EXE_PATH}")
        return

    # verify if the path even exists
    if os.path.isdir(SETTINGS_PATH):
        # // write now since path works
        os.makedirs("config", exist_ok=True)
        with open("config/settings.ini", "w") as file:
            file.write(f"PATH={SETTINGS_PATH}")
    else:
        print(f"Invalid Path. \nPath recieved {EXE_PATH}")
        return

    return SETTINGS_PATH


