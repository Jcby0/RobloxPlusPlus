# Imports

import os
import platform

# Mac and windows support

IS_WINDOWS=True

if platform.system() == "Darwin":
    IS_WINDOWS=False
elif platform.system() == "Windows":
    IS_WINDOWS=True
else:
    exit(1)

MAC_OS_PATH=f"{os.path.expanduser('~/Documents/RobloxPlusPlus')}"
WINDOWS_PATH=f"{os.getenv('APPDATA')}\\RobloxPlusPlus"

WINDOWS_ROBLOX_PATH=f"{os.getenv('LOCALAPPDATA')}\\Roblox\\Versions"
MAC_OS_ROBLOX_PATH="/Applications/Roblox.app/Contents"

for root, dirs, files in os.walk(WINDOWS_ROBLOX_PATH):
    if "RobloxPlayerBeta.exe" in files:
        WINDOWS_ROBLOX_PATH=root
MAX_FPS=1000
