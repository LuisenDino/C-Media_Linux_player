from App.AppFrames.MainFrame import MainFrame
import tkinter as tk
import json

root = tk.Tk()
with open("test.json", "r") as file:
    config = json.loads(file.read())
    
main = MainFrame(root, config)
root.mainloop()

