# Fps Management

import Constants
import json
import os

class FPS:

    fps = 60

    # Takes in value 0 -> 1
    def calculateFPS(value) -> None:
        FPS.fps = max(1, int(float(float(value)/1000)*Constants.MAX_FPS))

    def getFPSFromFile() -> float:
        if Constants.IS_WINDOWS:
            with open(f"{Constants.WINDOWS_ROBLOX_PATH}\\ClientSettings\\ClientAppSettings.json", "r") as f:
                try:
                    return json.load(f)["DFIntTaskSchedulerTargetFps"]
                except:
                    return None
        else:
            with open(f"{Constants.MAC_OS_ROBLOX_PATH}/ClientSettings/ClientAppSettings.json", "r") as f:
                try:
                    return json.load(f)["DFIntTaskSchedulerTargetFps"]
                except:
                    return None

    def getJSONFromFile() -> dict: 
        if Constants.IS_WINDOWS:
            with open(f"{Constants.WINDOWS_ROBLOX_PATH}\\ClientSettings\\ClientAppSettings.json", "r") as f:
                try:
                    return json.load(f)
                except:
                    return None
        else:
            with open(f"{Constants.MAC_OS_ROBLOX_PATH}/ClientSettings/ClientAppSettings.json", "r") as f:
                try:
                    return json.load(f)
                except:
                    return None

    def setClientFPS():
        data = FPS.getJSONFromFile()

        data["DFIntTaskSchedulerTargetFps"] = FPS.fps

        if Constants.IS_WINDOWS:
            with open(f"{Constants.WINDOWS_ROBLOX_PATH}\\ClientSettings\\ClientAppSettings.json", "w") as f:
                json.dump(data, f)
        else:
            with open(f"{Constants.MAC_OS_ROBLOX_PATH}/ClientSettings/ClientAppSettings.json", "w") as f:
                json.dump(data, f)


    
