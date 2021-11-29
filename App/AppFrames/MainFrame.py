import tkinter as tk
from .WebViewFrame import WebViewFrame
from .PrinterFrame import PrinterFrame
import json
from cefpython3 import cefpython as cef

class MainFrame(tk.Frame):
    """
    Clase de pantalla principal
    :param root: tk.Tk. aplicacion tkinter.
    :param config: dic. Configuracion de la aplicacion.
    """
    def __init__(self, root, controllers):
        """
        Constructor de clase
        :param root: tk.Tk. aplicacion tkinter.
        :param config: dic. Configuracion de la aplicacion.
        """
        self.webview_frame = None
        self.printer_frame = None
        self.controllers = controllers


        #MainFrame
        tk.Frame.__init__(self, root)
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
        self.master.bind("<Configure>", self.on_root_configure)
        self.bind("<Configure>", self.on_configure)
        
        self.apis = {}

        for controller in controllers:
            #PrinterFrame
            if "Control.Impresion.dll" in controller["NombreArchivo"]:
                self.printer_frame = PrinterFrame(controller["ObjetoBase"])
                self.apis["printer"] = self.printer_frame.get_printer()
            #BrowserFrame
            elif "Control.NavegadorWebChrome.dll" in controller["NombreArchivo"]:
                self.webview_frame = WebViewFrame(self, url=controller["ObjetoBase"]["UrlInicio"])
                self.webview_frame.grid(row=1, column=0,sticky=(tk.N + tk.S + tk.E + tk.W))

        tk.Grid.rowconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        if(self.webview_frame):
            cef.Initialize()

    def on_close(self):
        """
        Llama a los metodos de cierre
        El metodo se ejecuta al cerrar la aplicacion
        """
        if self.webview_frame:
            self.webview_frame.on_root_close()
        self.master.destroy()
        if(self.webview_frame):
            cef.Shutdown()  

    def on_root_configure(self, _):
        """
        Llama a los metodos de configuracion de la aplicacion
        Se ejecuta cuando se configura la aplicacion
        """
        if self.webview_frame:
            self.webview_frame.on_root_configure()
            self.webview_frame.load_apis(self.apis)
    
    def on_configure(self, event):
        """
        Llama a los metodos de configuracion de la vista
        se ejecuta cuando se configura la vista
        :param event: event. evento de configuracion
        """
        if self.webview_frame:
            width = event.width
            height = event.height
            self.webview_frame.on_mainframe_configure(width, height)

    def get_WebView_frame(self):
        """
        Obtiene el frame del contenedor web
        """
        return self.webview_frame

    def get_printer_frame(self):
        """
        Obtiene el frame de la impresora
        """
        return self.printer_frame
        
