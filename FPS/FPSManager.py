# Fps Management

import Constants

class FPS:

    # Takes in value 0 -> 1
    def calculateFPS(value) -> int:
        return max(30, int(float(value)*Constants.MAX_FPS))

    def getFPSFromFile(value) -> None:
        pass

    def getClientSettingsLocation() -> None:
        pass

    def setClientFPS(fps):
        pass


    
