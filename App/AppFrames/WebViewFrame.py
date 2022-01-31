import logging
import threading
import tkinter as tk #Librería GUI
from cefpython3 import cefpython as cef #Librería Chromium Embeded Framework
from .JSBridge import JSBridge #Clase que permite la interaccipn entre la url y la aplicacion local
from .NavBar import NavigationBar
#from .EventHandler import EventHandler

class WebViewFrame(tk.Frame):
    """
    Clase de Contenedor Web
    :param parent: tk.Frame. tk.Tk. Frame o ventana donde sera anadido el contenedor
    :param url: str. url del html (Para archivos 'file://{ubicacion}')
    """
 
    def __init__(self, parent, settings):
        """
        Constructor de Clase
        :param parent: tk.Frame. tk.Tk. Frame o ventana donde sera anadido el contenedor
        :param url: str. url del html (Para archivos 'file://{ubicacion}')
        """
        self.closing = False
        self.browser = None
        self.nav_bar = None
        self.settings = settings
        self.parent = parent
        
        #self.event_handler = None
        #self.event_handler = EventHandler()

        if self.settings["MostrarBarraNavegacion"]:
            self.nav_bar = NavigationBar(self.parent)
            self.nav_bar.grid(row=0, column=0, sticky= (tk.E + tk.W))

        self.url = settings["UrlInicio"]
        tk.Frame.__init__(self, parent)
        self.configure(bg="blue")
        self.bind("<Configure>", self.on_configure)
        

    def embed_browser(self):
        """
        Funcion para embeber el contenedor web
        """        
        window_info = cef.WindowInfo()  #Informacion de contenedor CEF
        rect = [0, 0, self.winfo_width(), self.winfo_height()]  #Informacion del rectangulo del frame del contenedor CEF [Left, Top, Right, Bottom]
        window_info.SetAsChild(self.winfo_id(), rect) #Crea el navegador como una ventana/vista hijo
        self.config(bg="red")
        rect
        settings = {
            "background_color" : 0xc93c20
        }
        try:
            self.browser = cef.CreateBrowserSync(window_info, url=self.url, settings=settings) #Creacion del navegador
        except Exception as e:
            logging.error(str(e))
        assert self.browser

        if self.nav_bar:
            self.nav_bar.set_browser(self.browser)
        
        self.message_loop_work()
    
    def message_loop_work(self):
        """
        Realiza una iteracion de CEF message loop processing.
        Recursiva.
        """
        cef.MessageLoopWork()
        self.after(10, self.message_loop_work)

    def on_configure(self, _):
        """
        Si no existe un navegador creado ejecuta embed_browser.
        Se ejecuta al cargar la vista.
        """
        if not self.browser:
            self.embed_browser()
            

    def on_mainframe_configure(self, width, height):
        """        
        Notifica al navegador cambios en la ventana principal
        Se ejecuta al modificar la ventana principal.
        """
        if self.browser:
            self.browser.SetBounds(0,0,width, height)
            self.browser.NotifyMoveOrResizeStarted()

    def on_root_configure(self):
        """
        Notifica al navegador cambios en la ventana principal
        Se ejecuta al modificar la ventana superior.
        """
        if self.browser:
            self.browser.NotifyMoveOrResizeStarted()

    def load_apis(self, apis):
        """
        Carga un objeto api al navegador
        :param apis: dic. objetos controladores con los metodos que sera enviado al navegador
        """
        if self.browser:    
            self.js_bridge = JSBridge(self.browser, apis)
            #self.event_handler.set_apis(apis)
            self.browser.SetClientHandler(LoadHandler(self.js_bridge.parse_api_js(), apis, self.nav_bar))
            bindings = cef.JavascriptBindings(bindToFrames=True, bindToPopups=True)
            bindings.SetObject("external", self.js_bridge)
            self.browser.SetJavascriptBindings(bindings)

    def on_root_close(self):
        """
        Llamada al cerrar la aplicacion superior
        """
        if self.browser:
            #self.event_handler.kill()
            self.browser.CloseBrowser(True)            
            self.clear_browser_references()
            
            
    
    def clear_browser_references(self):
        """
        Limpia las referencias del navegador
        """
        self.browser = None



class LoadHandler(object):
    """
    Clase de manejo de carga del navegador
    :param script: str. script de inicio del navegador
    """
    def __init__(self, script, apis, nav_bar = None):
        """
        Constructor de clase
        :param script: str. script de inicio del navegador
        """
        self.script = script
        self.apis = apis
        self.nav_bar = nav_bar
        #self.event_handler = event_handler


    def OnLoadingStateChange(self, browser, is_loading, **_):
        """
        Carga las funciones cuando se inicia la aplicacion web
        :param browser: navegador que ejecutara los comandos
        :param is_loading: bool. bandera de carga del navegador
        :params **_: parametros adicionales de carga del navegador
        """
        if not is_loading:
            browser.GetJavascriptBindings().Rebind()
            browser.ExecuteJavascript(self.script)
            #self.event_handler.set_browser(browser)
            for api in list(self.apis.values()):
                api.get_event().set_browser(browser)
        
    def OnLoadStart(self, browser, **_):
        if self.nav_bar:
            self.nav_bar.set_url(browser.GetUrl())

              
