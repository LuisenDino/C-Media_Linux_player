from tkinter import messagebox
import tkinter as tk
#from ConfigGUI.MainFrame import MainFrame
from App.ConfigGUI.MainFrame import MainFrame
import logging
import sys
import os


def main():
    """
    Funcion de inicio de la aplicacion en modo de configuracion
    """
    
    root = tk.Tk(className="C-Media Player configuration")
    try:
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/LOGO-CMedia.png"
        icon = tk.PhotoImage(file=path)   
        root.tk.call('wm', 'iconphoto', root._w, icon)
    except Exception as e:
        logging.error(str(e))
    root.title("C-Media Player - Configuración")
    #root.geometry("485x360")
    root.configure(bg="#eef1f2")
    config_frame = MainFrame(root)
    config_frame.mainloop()
    
if __name__ == "__main__":
    main()