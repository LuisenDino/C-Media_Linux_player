import logging
#from AppFrames.MainFrame import MainFrame
from App.AppFrames.MainFrame import MainFrame
import json
import tkinter as tk
import os
import sys

def main(splash):
    """
    Funcion de inicio de la aplicacion    
    """
    pantallas = {}
    sett = get_sett()
    screen_config = get_screen_config(sett["Ruta"])
    splash.destroy()
    root = tk.Tk(className="C-Media Player")
    root.attributes("-fullscreen", sett["PantallaCompleta"])
    root.attributes("-topmost", sett["SiempreVisible"])
    if not(sett["MostrarBordeVentana"]):
        root.overrideredirect(1)    
    root.geometry(str(sett["AnchoRequerido"])+"x"+str(sett["AltoRequerido"])+"+"+str(sett["LeftRequerido"])+"+"+str(sett["TopRequerido"]))
    
    try:
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/LOGO-CMedia.png"
        icon = tk.PhotoImage(file=path)   
        root.tk.call('wm', 'iconphoto', root._w, icon)
    except Exception as e:
        logging.error(str(e))

    for pantalla in screen_config["Pantallas"]:
        pantallas[pantalla["ScreenNumber"]] = MainFrame(root, pantalla["Controles"])
        if(pantalla["ScreenNumber"]==1):
          root.title(pantalla["TitleName"])
    
    #pantallas[1].mainloop() 
    


def get_screen_config(ruta):
    """
    Obtiene la informacion de las pantallas y su configuracion
    :param ruta: str. Ruta donde se encuentra el archivo de configuracion
    :return: dic. Configuracion extraida del archivo json
    """
    try:
        with open(ruta, 'r', encoding="utf-8-sig") as file:
            screen_config = json.load(file)
        return screen_config
    except Exception as e:
        logging.error(str(e))
        return str(e)

def get_sett():
    """
    Obtiene la informacion de configuracion de la aplicacion
    :return: dic. Configuracion extraida del archivo json
    """
    path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/configs/config.json"
    try:
        with open(path, "r") as file:
            sett = json.load(file)
        return sett
    except Exception as e:
        logging.error(str(e))
        return str(e)

if __name__ == "__main__":
    main()
