import tkinter as tk

class PrinterFrame(tk.Frame):
    """
    Clase de controlador de impresora
    :param settings: Configuracion de la impresora
    """

    def __init__(self, settings):
        """
        Constructor de clase
        :param settings: Configuracion de la impresora
        """
        if settings["TipoImpresora"] == 0:
            from .Controllers.Printers.TM_T88V import Printer
        else:
            raise Exception("No existe controlador para la impresora seleccionada")
        self.printer = Printer({"id_vendor":"0x04b8", "id_product": "0x0202"}, True)

    def get_printer(self):
        """
        Obtiene la impresora
        """
        return self.printer
