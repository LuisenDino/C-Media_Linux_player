from cefpython3 import cefpython as cef
import tkinter as tk
from App.AppFrames.Controllers.CodeReaders.Honeywell3320g import BarCodeReader


url = "file:///home/luis/Escritorio/C-Media_Linux_player/example.html"


cef.Initialize()
browser = cef.CreateBrowserSync(url=url)

bindings = cef.JavascriptBindings(bindToFrames=True, bindToPopups=True)
reader = BarCodeReader({"port":"/dev/ttyACM0"})
bindings.SetObject("printer", reader)
browser.SetJavascriptBindings(bindings)

cef.MessageLoop()



