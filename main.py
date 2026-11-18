from components import get_path
from components import gui


import os
SETTINGS_PATH = get_path.get_path()
os.makedirs("config", exist_ok=True)

gui.rungui(SETTINGS_PATH)