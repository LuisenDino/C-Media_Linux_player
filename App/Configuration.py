from tkinter import messagebox
import tkinter as tk
from App.ConfigGUI.MainFrame import MainFrame
import pathlib
import logging

def main():
    """
    Funcion de inicio de la aplicacion en modo de configuracion
    """
    #messagebox.showinfo(message=str(pathlib.Path().absolute()), title=str(pathlib.Path(__file__).absolute().name))
    
    root = tk.Tk()
    try:
        icon = tk.PhotoImage(file='Media/LOGO-CMedia.png')   
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