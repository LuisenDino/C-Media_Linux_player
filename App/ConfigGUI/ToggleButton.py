import tkinter as tk
class ToggleButton(tk.Frame):
    """
    Clase de modelo de ToggleButton
    :param parent: tk.Frame. Vista padre
    :param boolVar: tk.BooleanVar. Variable donde se guardara el valor del ToggleButton
    """

    def __init__(self, parent, boolVar):
        """
        Constructor de Clase
        :param parent: tk.Frame. Vista padre
        :param boolVar: tk.BooleanVar. Variable donde se guardara el valor del ToggleButton
        """ 
        self.boolVar = boolVar
        tk.Frame.__init__(self, parent)
        self.off = tk.Button(self, text="off", state="active", command=self.toggle)
        self.on =  tk.Button(self, text="on", state="disabled", command=self.toggle)
        if boolVar.get():
                self.off.configure(state="disabled")
                self.on.configure(state="active")    
        else:
            self.on.configure(state="disabled")
            self.off.configure(state="active")
        self.on.grid(row=0, column=0, sticky="nsew")
        self.off.grid(row=0, column=1, sticky="nsew")

    def toggle(self):
        """
        Cambia el estado de la variable y del toggleButton
        """
        if self.boolVar:
            self.boolVar.set(not self.boolVar.get())
            if self.off["state"] == "active":
                self.off.configure(state="disabled")
                self.on.configure(state="active")
            elif self.on["state"] == "active":
                self.on.configure(state="disabled")
                self.off.configure(state="active")




