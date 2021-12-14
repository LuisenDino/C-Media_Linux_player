import tkinter as tk


class CodeReaderFrame(tk.Frame):
    def __init__(self, settings):
        """
        Constructor de clase
        :param settings: Configuracion del lector
        """
        
        from .Controllers.CodeReaders.Honeywell3320g import BarCodeReader
        
        self.code_reader = BarCodeReader({"port":"/dev/ttyACM0"})

    def get_code_reader(self):
        """
        Obtiene el lector
        """
        return self.code_reader


