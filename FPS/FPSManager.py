# Fps Management

import Constants
import json

class FPS:

    fps = 60

    # Takes in value 0 -> 1
    def calculateFPS(value) -> None:
        FPS.fps = max(1, int(float(float(value)/1000)*Constants.MAX_FPS))

    def getFPSFromFile() -> float | None:
        with open(f"{Constants.MAC_OS_ROBLOX_PATH}/ClientSettings/ClientAppSettings.json", "r") as f:
            try:
                return json.load(f)["DFIntTaskSchedulerTargetFps"]
            except:
                return None
            
    def setClientFPS():
        data = { "DFIntTaskSchedulerTargetFps": FPS.fps }
        with open(f"{Constants.MAC_OS_ROBLOX_PATH}/ClientSettings/ClientAppSettings.json", "w") as f:
            json.dump(data, f)


    
