import Constants
import os

def createCustomDir() -> None:
    if Constants.IS_WINDOWS:
        if os.path.isfile(Constants.WINDOWS_PATH):
            if not os.path.exists(Constants.WINDOWS_PATH):
                os.mkdir(Constants.WINDOWS_PATH)
    else:
        if not os.path.exists(Constants.MAC_OS_PATH):
            os.mkdir(Constants.MAC_OS_PATH)

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
                