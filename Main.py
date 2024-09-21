# TODO #1
# Macos path
# Add FPS Class/Finish it
#
# TODO #2
# Asset editing
# Research other client settings etc
# Do own research by searching roblox files
# Find a operating sytem friendly file extension or do .exe and some other one for mac
#


# Imports

import tkinter
from tkinter import ttk
import tkinter.font
import sv_ttk
from FPS.FPSManager import FPS
import Constants

# Application Class

class Application:
    
    def __init__(self, Name, Width, Height, Resizable=False) -> None:
        self.Name = Name
        self.Width = Width
        self.Height = Height
        self.Resizable = Resizable
        self.createWindow()
    
    def createWindow(self) -> None:
        self.root = tkinter.Tk(self.Name)
        self.root.title(self.Name)
        self.root.geometry(f"{self.Width}x{self.Height}")
        if not self.Resizable:
            self.root.resizable(0, 0)
            self.root.maxsize(self.Width, self.Height)
            self.root.minsize(self.Width, self.Height)

    def getWindow(self) -> tkinter.Tk:
        return self.root

main = Application("Roblox++", 400, 300)



# FPS Button

main.fpsBtn = ttk.Button(main.root, text="Set FPS Cap", command=None)
main.fpsBtn.grid(column=1, row=4)

def updateFPS(percentage):
    fps = FPS.calculateFPS(float(percentage)/1000)
    print(fps)

# Fps Cap
main.fpsCap = ttk.LabeledScale(main.root, variable=None, from_=30, to=999, padding=2)
main.fpsCap.grid(column=1, row=2)
main.fpsCap.scale.config(command=updateFPS)


# Set the theme of window
sv_ttk.set_theme("dark")

# Run the loop (keep window open)
main.root.mainloop()