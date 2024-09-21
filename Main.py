# TODO #1
# Positioning items in frame
# Cleaner UI
# Macos path
# Differentiate systems
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
import sv_ttk

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
            self.root.maxsize(self.Width, self.Height)
            self.root.minsize(self.Width, self.Height)

    def getWindow(self) -> tkinter.Tk:
        return self.root

main = Application("Roblox++", 400, 300)

# Label
main.fpsLabel = ttk.Label(main.root, text="FPS Cap")
main.fpsLabel.pack()

# Fps Cap
main.fpsCap = ttk.Scale(main.root)
main.fpsCap.pack()

# Set the theme of window
sv_ttk.set_theme("dark")

# Run the loop (keep window open)
main.root.mainloop()