import tkinter as tk
from tkinter import messagebox

class CodeReaderFrame(tk.Frame):
    def __init__(self, settings):
        """
        Constructor de clase
        :param settings: Configuracion del lector
        """
        
        from .Controllers.CodeReaders.Honeywell3320g import BarCodeReader
        
        self.code_reader = BarCodeReader(settings["PuertoSerial"])

    def get_code_reader(self):
        """
        Obtiene el lector
        """
        return self.code_reader


