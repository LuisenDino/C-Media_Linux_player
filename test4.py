from cefpython3 import cefpython as cef
import tkinter as tk

url = "file:///home/luis/Escritorio/C-Media_Linux_player/example.html"

class Printer():
    def __init__(self):
        pass

    def get_paper(self):
        #js_callback.Call(10)
        return "hola"




cef.Initialize()
browser = cef.CreateBrowserSync(url=url)

bindings = cef.JavascriptBindings(bindToFrames=True, bindToPopups=True)
printer = Printer()
print(dir(printer))
bindings.SetObject("printer", printer)
browser.SetJavascriptBindings(bindings)

cef.MessageLoop()



