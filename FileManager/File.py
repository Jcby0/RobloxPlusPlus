import Constants
import os
import requests

def createCustomDir() -> None:
    if Constants.IS_WINDOWS:
        if not os.path.exists(Constants.WINDOWS_PATH):
            os.mkdir(Constants.WINDOWS_PATH)
    else:
        if not os.path.exists(Constants.MAC_OS_PATH):
            os.mkdir(Constants.MAC_OS_PATH)

def downloadAssets() -> None:
    if Constants.IS_WINDOWS:
        if not os.path.isfile(f"{Constants.WINDOWS_PATH}\\rblx.ico"):
            r = requests.get("https://raw.githubusercontent.com/Jcby0/RobloxPlusPlus/refs/heads/master/Assets/rblx.ico")
            with open(f"{Constants.WINDOWS_PATH}\\rblx.ico", "wb") as f:
                f.write(r.content)
    else:
        if not os.path.isfile(f"{Constants.MAC_OS_PATH}/rblx.ico"):
            r = requests.get("https://raw.githubusercontent.com/Jcby0/RobloxPlusPlus/refs/heads/master/Assets/rblx.ico")
            with open(f"{Constants.MAC_OS_PATH}/rblx.ico", "wb") as f:
                f.write(r.content)

def robloxDirExists() -> bool:
    if Constants.IS_WINDOWS:
        return os.path.exists(Constants.WINDOWS_ROBLOX_PATH)
    return os.path.exists(Constants.MAC_OS_ROBLOX_PATH)

def createClientSettings() -> None:
    if Constants.IS_WINDOWS:
        if not os.path.exists(f"{Constants.WINDOWS_ROBLOX_PATH}/ClientSettings"):
            os.mkdir(f"{Constants.WINDOWS_ROBLOX_PATH}/ClientSettings")
    else:
        if not os.path.exists(f"{Constants.MAC_OS_ROBLOX_PATH}/ClientSettings"):
            os.mkdir(f"{Constants.MAC_OS_ROBLOX_PATH}/ClientSettings")
                