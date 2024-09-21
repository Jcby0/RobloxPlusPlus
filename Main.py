# Add FPS Class/Finish it TODO
# TODO #2
# Asset editing
# Research other client settings etc
# Do own research by searching roblox files
# Find a operating sytem friendly file extension or do .exe and some other one for mac
#

# Resources
#  https://github.com/MaximumADHD/Roblox-FFlag-Tracker/tree/main
#  https://github.com/catb0x/Roblox-Potato-FFlags
#  Potato mode idea


# Imports

import tkinter
from tkinter import ttk
import tkinter.font
import sv_ttk
from FPS.FPSManager import FPS
import Constants
import FileManager.File as File


# Check Files

File.createCustomDir()

if File.robloxDirExists():
    File.createClientSettings()

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

main = Application("", 200, 100)
main.root.iconbitmap("Assets/rblx.ico")

# Fps Cap
main.fpsCap = ttk.LabeledScale(main.root, variable=None, from_=1, to=999, padding=2)
main.fpsCap.pack()
main.fpsCap.scale.config(command=FPS.calculateFPS)
main.fpsCap.value = FPS.getFPSFromFile() or 60 # load in fps from file

# FPS Button
main.fpsBtn = ttk.Button(main.root, text="Set FPS Cap", command=FPS.setClientFPS, style="")
main.fpsBtn.pack()

# Set the theme of window
sv_ttk.set_theme("dark")

# Run the loop (keep window open)
main.root.mainloop()