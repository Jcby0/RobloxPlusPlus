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
            if os.path.exists(f"{Constants.WINDOWS_ROBLOX_PATH}\\ClientSettings\\ClientAppSettings.json"):
                with open(f"{Constants.WINDOWS_ROBLOX_PATH}\\ClientSettings\\ClientAppSettings.json", "r") as f:
                    try:
                        FPS.fps = json.load(f)["DFIntTaskSchedulerTargetFps"]
                        return FPS.fps
                    except Exception as e:
                        print(e)
                        return 60
        else:
            if os.path.exists(f"{Constants.MAC_OS_ROBLOX_PATH}/MacOS/ClientSettings/ClientAppSettings.json"):
                with open(f"{Constants.MAC_OS_ROBLOX_PATH}/MacOS/ClientSettings/ClientAppSettings.json", "r") as f:
                    try:
                        FPS.fps = json.load(f)["DFIntTaskSchedulerTargetFps"]
                        return FPS.fps
                    except:
                        return 60

    def getJSONFromFile() -> dict: 
        if Constants.IS_WINDOWS:
            if os.path.exists(f"{Constants.WINDOWS_ROBLOX_PATH}\\ClientSettings\\ClientAppSettings.json"):
                with open(f"{Constants.WINDOWS_ROBLOX_PATH}\\ClientSettings\\ClientAppSettings.json", "r") as f:
                    try:
                        return json.load(f)
                    except:
                        return None
        else:
            if os.path.exists(f"{Constants.MAC_OS_ROBLOX_PATH}/MacOS/ClientSettings/ClientAppSettings.json"):
                with open(f"{Constants.MAC_OS_ROBLOX_PATH}/MacOS/ClientSettings/ClientAppSettings.json", "r") as f:
                    try:
                        return json.load(f)
                    except:
                        return None

    def setClientFPS(fps=0):
        if fps != 0:
            FPS.fps = fps

        data = FPS.getJSONFromFile()

        if data == None:
            data = {}

        data["DFIntTaskSchedulerTargetFps"] = FPS.fps

        if Constants.IS_WINDOWS:
            with open(f"{Constants.WINDOWS_ROBLOX_PATH}\\ClientSettings\\ClientAppSettings.json", "w") as f:
                json.dump(data, f)
        else:
            with open(f"{Constants.MAC_OS_ROBLOX_PATH}/ClientSettings/ClientAppSettings.json", "w") as f:
                json.dump(data, f)


    
