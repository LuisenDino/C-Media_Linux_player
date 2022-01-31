class Event():  
    def __init__(self, nombre_js):
        self.value = False
        self.nombre_js = nombre_js
        self.function = ""
        self.params = ""
        self.browser = None

    def awake(self, function, params):
        """
        Enciende el evento
        :param function: nombre de la funcion a llamar en js
        :param params: list. Lista de los parametros a la funcion js
        """
        self.value = True
        self.function = function
        self.params = params
        if self.browser:
            js = "Ciel.MPC.WebPlayer.Controles."+self.nombre_js+"."+self.function+"("+",".join(self.params)+")"
            self.browser.ExecuteJavascript(js)
            self.clear_event()

    def clear(self):
        self.value = False
        self.function = ""
        self.params = ""

    def get(self):
        return self.value

    def set_browser(self, browser):
        self.browser = browser