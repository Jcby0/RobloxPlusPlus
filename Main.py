# TODO 
# Asset editing
# * Edit roblox icon in taskbar (will need to add assets)
#   * Add multiple options (dropdown)
# Research other client settings etc
# Do own research by searching roblox files
# Find a operating sytem friendly file extension or do .exe and some other one for mac
#

# Resources
#  https://github.com/MaximumADHD/Roblox-FFlag-Tracker/tree/main
#  https://github.com/catb0x/Roblox-Potato-FFlags
#  Potato mode idea


# Imports

from FPS.FPSManager import FPS
import Constants
import FileManager.File as File
import customtkinter

# Check Files

File.createCustomDir()

if File.robloxDirExists():
    File.createClientSettings()

File.downloadAssets()

# Application Class

class Application:
    
    def __init__(self, Name, Width, Height, Resizable=False) -> None:
        self.Name = Name
        self.Width = Width
        self.Height = Height
        self.Resizable = Resizable
        self.createWindow()
    
    def createWindow(self) -> None:
        self.root = customtkinter.CTk()
        self.root.title(self.Name)
        self.root.geometry(f"{self.Width}x{self.Height}")
        if not self.Resizable:
            self.root.resizable(0, 0)
            self.root.maxsize(self.Width, self.Height)
            self.root.minsize(self.Width, self.Height)

main = Application("", 290, 100)

# Set Icon
if Constants.IS_WINDOWS:
    main.root.iconbitmap(f"{Constants.WINDOWS_PATH}\\rblx.ico")
else:
    pass
    #main.root.iconbitmap(f"{Constants.MAC_OS_PATH}\\rblx.icns")

# Fps Cap
main.fpsLabel = customtkinter.CTkLabel(main.root, text=f"FPS Cap")
main.fpsLabel.grid(column=1, row=1, padx=8)

main.fpsCap = customtkinter.CTkTextbox(main.root, width=60, height=5, wrap="none", activate_scrollbars=False)
main.fpsCap.grid(column=2, row=1, pady=8)

# Loading From File
loadedFPS = FPS.getFPSFromFile()
main.fpsCap.insert("1.0", f"{loadedFPS}")

def setClientFPS() -> None:

    fps = str(main.fpsCap.get("1.0", "1.end"))
    
    if fps.isnumeric():
        FPS.setClientFPS(fps)
    else:
        main.fpsCap.delete("1.0", "1.end")
        main.fpsCap.insert("1.0", "Invalid Number")

# FPS Button
main.fpsBtn = customtkinter.CTkButton(main.root, text="Set FPS Cap", command=setClientFPS)
main.fpsBtn.grid(column=3, row=1, padx=8)

# Icon MACOS ONLY RN

def selectFile():
    if not Constants.IS_WINDOWS:
        file = customtkinter.filedialog.askopenfile(filetypes=[("ICNS Icon File", "*.icns")])

            
        f = open(file.name, "rb")
        data = f.read()
        f.close()
        with open(f"{Constants.MAC_OS_ROBLOX_PATH}/Resources/AppIcon.icns", "wb") as f:
            f.write(data)
            print("wrote")


main.iconText = customtkinter.CTkLabel(main.root, text=f"Roblox Icon")
main.iconText.grid(column=1, row=2, padx=4)

main.iconFile = customtkinter.CTkButton(main.root, text = "Choose file", command = selectFile)
main.iconFile.grid(column=3, row=2)

# Run the loop (keep window open)
main.root.mainloop()