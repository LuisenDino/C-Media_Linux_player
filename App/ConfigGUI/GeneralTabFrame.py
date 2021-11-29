import tkinter as tk
from tkinter import Variable, ttk
import json
from tkinter.filedialog import askopenfilename
from .ToggleButton import ToggleButton

class GeneralTabFrame(tk.Frame):
    """
    Clase de vista de configuracion General
    :param parent: tk.Frame. vista padre.
    """
    def __init__(self, parent):
        """
        Constructor de clase
        :param parent: tk.Frame. vista padre.
        """
        self.settings = {}
        self.get_settings()
        tk.Frame.__init__(self, parent)
        self.configure(bg="#eef1f2")
        self.file_name = tk.StringVar()
        self.file_name.set(self.settings["Ruta"])
        self.fullscreen = tk.BooleanVar()
        self.fullscreen.set(self.settings["PantallaCompleta"])
        self.window_border = tk.BooleanVar()
        self.window_border.set(self.settings["MostrarBordeVentana"])
        self.on_top = tk.BooleanVar()
        self.on_top.set(self.settings["SiempreVisible"])

        #Fila 1
        tk.Label(self, text="Archivo de recursos:", bg="#eef1f2", ).grid(column=0, row=0, columnspan=2)
        tk.Entry(self, width=33, state="readonly", textvariable=self.file_name).grid(row=0, column=2, columnspan=5,padx=10)
        tk.Button(self, command=self.select_file, text="...").grid(row=0, column=7, pady=15)

        #Fila 2
        tk.Label(self, text="Pantalla completa:", bg="#eef1f2" ).grid(column=0, row=1, columnspan=2)
        ToggleButton(self, self.fullscreen).grid(column=2, row=1, columnspan=2, padx=0)
        
        #Fila 3
        tk.Label(self, text="Borde ventana:", bg="#eef1f2" ).grid(column=0, row=2, columnspan=2)
        ToggleButton(self, self.window_border).grid(column=2, row=2, columnspan=2, padx=0)

        #Fila 4
        tk.Label(self, text="Siempre visible:", bg="#eef1f2" ).grid(column=0, row=3, columnspan=2)
        ToggleButton(self, self.on_top).grid(column=2, row=3, columnspan=2, padx=0)
        

        #Fila 5
        tk.Label(self, text="Ancho", bg="#eef1f2" ).grid(column=0, row=4, columnspan=1)
        self.width= tk.StringVar()
        self.width.set(self.settings["AnchoRequerido"])
        tk.Entry(self,width=5 , textvariable=self.width).grid(column=1, row=4, columnspan=1)
        tk.Label(self, text="Alto", bg="#eef1f2" ).grid(column=2, row=4, columnspan=1)
        self.height = tk.StringVar()
        self.height.set(self.settings["AltoRequerido"])
        tk.Entry(self,width=5, textvariable=self.height).grid(column=3, row=4, columnspan=1)
        tk.Label(self, text="Superior", bg="#eef1f2" ).grid(column=4, row=4, columnspan=1)
        self.top= tk.StringVar()
        self.top.set(self.settings["TopRequerido"])
        tk.Entry(self,width=5, textvariable=self.top).grid(column=5, row=4, columnspan=1)
        tk.Label(self, text="Izquierda", bg="#eef1f2" ).grid(column=6, row=4, columnspan=1)
        self.left = tk.StringVar()
        self.left.set(self.settings["LeftRequerido"])
        tk.Entry(self,width=5, textvariable=self.left).grid(column=7, row=4, columnspan=1)

        #Fila 6
        tk.Button(self,text="Guardar", command=self.save).grid(column=0, row=5, columnspan=7)

        #Imagen
        img = tk.PhotoImage(file="App/Media/cog_edit.png")
        tk.Label(self, image=img, bg="#eef1f2").grid(row = 6, column = 7, sticky="e", pady=5)

    
    def select_file(self):
        """
        Abre un selector de archivos y guarda el valor en una atributo
        """
        self.file_name.set(askopenfilename())

    def save(self):
        """
        Guarda la informacion en el archivo json de configuracion
        """
        with open("App/Media/config.json", "w") as file:
            settings = {
                "Ruta" : self.file_name.get(),
                "PantallaCompleta" : self.fullscreen.get(), 
                "SiempreVisible" : self.on_top.get(),
                "MostrarBordeVentana" : self.window_border.get(), 
                "AnchoRequerido" : int(self.width.get()),
                "AltoRequerido" : int(self.height.get()),
                "TopRequerido" : int(self.top.get()),
                "LeftRequerido" : int(self.left.get())
            }

            file.write(json.dumps(settings))

    def get_settings(self):
        """
        Obtiene la configuracion del archivo json y las guarda en un atributo de la clase
        """
        with open("App/Media/config.json", "r") as file:
            self.settings = json.loads(file.read())