from AppFrames.MainFrame import MainFrame
import json
import tkinter as tk
import os
import sys
import pathlib

def solve_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, )
    return os.path.join(os.path.abspath('.'), relative_path)


def main():
    """
    Funcion de inicio de la aplicacion    
    """
    pantallas = {}
    sett = get_sett()
    screen_config = get_screen_config(sett["Ruta"])

    root = tk.Tk()

    root.attributes("-fullscreen", sett["PantallaCompleta"])
    root.attributes("-topmost", sett["SiempreVisible"])
    if not(sett["MostrarBordeVentana"]):
        root.overrideredirect(1)    
    root.geometry(str(sett["AnchoRequerido"])+"x"+str(sett["AltoRequerido"])+"+"+str(sett["LeftRequerido"])+"+"+str(sett["TopRequerido"]))


    icon = tk.PhotoImage(file='App/Media/LOGO-CMedia.png')   
    root.tk.call('wm', 'iconphoto', root._w, icon)

    for pantalla in screen_config["Pantallas"]:
        pantallas[pantalla["ScreenNumber"]] = MainFrame(root, pantalla["Controles"])
        if(pantalla["ScreenNumber"]==1):
          root.title(pantalla["TitleName"])
    pantallas[1].mainloop()


def get_screen_config(ruta):
    """
    Obtiene la informacion de las pantallas y su configuracion
    :param ruta: str. Ruta donde se encuentra el archivo de configuracion
    :return: dic. Configuracion extraida del archivo json
    """
    with open(ruta, 'r', encoding="utf-8-sig") as file:
        screen_config = json.load(file)
    return screen_config

def get_sett():
    """
    Obtiene la informacion de configuracion de la aplicacion
    :return: dic. Configuracion extraida del archivo json
    """
    path = solve_path("../config/config.json") 
    print(os.listdir(pathlib.Path(__file__).parent.resolve()))
    with open("App/Media/config.json", "r") as file:
        sett = json.load(file)
    return sett

if __name__ == "__main__":
    main()
