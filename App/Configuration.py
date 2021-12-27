from tkinter import messagebox
import tkinter as tk
#from ConfigGUI.MainFrame import MainFrame
from App.ConfigGUI.MainFrame import MainFrame
import logging
import sys
import os

def solve_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)

def main():
    """
    Funcion de inicio de la aplicacion en modo de configuracion
    """
    #messagebox.showinfo(message=str(pathlib.Path().absolute()), title=str(pathlib.Path(__file__).absolute().name))
    
    root = tk.Tk()
    try:
        path = solve_path('Media/LOGO-CMedia.png')
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