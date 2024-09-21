import Constants
import os

def createCustomDir() -> None:
    if Constants.IS_WINDOWS:
        if os.path.isfile(Constants.WINDOWS_PATH):
            if os.path.exists(Constants.WINDOWS_PATH):
                pass
            else:
                os.mkdir(Constants.WINDOWS_PATH)
    else:
        if os.path.exists(Constants.MAC_OS_PATH):
            pass
        else:
            os.mkdir(Constants.MAC_OS_PATH)

def robloxDirExists() -> bool:
    if Constants.IS_WINDOWS:
        pass
    return os.path.exists(Constants.MAC_OS_ROBLOX_PATH)

def createClientSettings() -> None:
    if Constants.IS_WINDOWS:
        pass
    else:
        if not os.path.exists(f"{Constants.MAC_OS_ROBLOX_PATH}/ClientSettings"):
            os.mkdir(f"{Constants.MAC_OS_ROBLOX_PATH}/ClientSettings")
                