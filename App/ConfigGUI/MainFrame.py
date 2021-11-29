import tkinter as tk
from tkinter import ttk
from .GeneralTabFrame import GeneralTabFrame

class MainFrame(tk.Frame):
    """
    Clase de pantalla principal (configuracion)
    :param root: tk.Tk. aplicacion tkinter.
    """
    def __init__(self, root):
        """
        Constructor de clase
        :param root: tk.Tk. aplicacion tkinter.
        """
        tk.Frame.__init__(self, root)
        self.configure(bg="#eef1f2")
        style =  ttk.Style()
        style.theme_create( "Config", parent="alt", settings={
            "TNotebook": {
                    "configure":{
                        "background": "#eef1f2"
                    }
                }, 
            "TNotebook.Tab":{
                "configure" :{
                    "background":"#eef1f2"
                }, 
                "map":{
                    "background": [("selected", "#dbdee1")]
                }
            }
        })

        style.theme_use("Config")
        
        #Creacion tabbed pane
        self.tabbed_pane = ttk.Notebook(root)

        #General Frame
        self.general_tab = GeneralTabFrame(self.tabbed_pane)
        """
        #Manager Frame
        self.manager_tab = tk.Frame(self.tabbed_pane)

        #Metadata Frame
        self.metadata_tab = tk.Frame(self.tabbed_pane)

        #logs Frame
        self.logs_tab = tk.Frame(self.tabbed_pane)
        """
        self.tabbed_pane.add(self.general_tab, text="General")
        #self.tabbed_pane.add(self.manager_tab, text="C-Media Manager")
        #self.tabbed_pane.add(self.metadata_tab, text="Metadatos")
        #self.tabbed_pane.add(self.logs_tab, text="Logs")
        self.tabbed_pane.pack(padx=5, pady=5, fill="both")

