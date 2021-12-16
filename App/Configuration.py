
import tkinter as tk
from App.ConfigGUI.MainFrame import MainFrame

def main():
    """
    Funcion de inicio de la aplicacion en modo de configuracion
    """
    root = tk.Tk()
    icon = tk.PhotoImage(file='Media/LOGO-CMedia.png')   
    root.tk.call('wm', 'iconphoto', root._w, icon)
    root.title("C-Media Player - Configuración")
    #root.geometry("485x360")
    root.configure(bg="#eef1f2")
    config_frame = MainFrame(root)
    config_frame.mainloop()
    
if __name__ == "__main__":
    main()