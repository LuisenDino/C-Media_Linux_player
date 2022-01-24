from App.AppFrames.CodeReaderFrame import CodeReaderFrame
import tkinter as tk

root = tk.Tk()
a = CodeReaderFrame({"port": "/dev/ttyACM1"})
root.mainloop()

