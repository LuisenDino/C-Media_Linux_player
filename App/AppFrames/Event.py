class Event():  
    def __init__(self, nombre_js):
        self.value = False
        self.nombre_js = nombre_js
        self.function = ""
        self.params = ""

    def awake(self, function, params):
        """
        Enciende el evento
        :param function: nombre de la funcion a llamar en js
        :param params: list. Lista de los parametros a la funcion js
        """
        self.value = True
        self.function = function
        self.params = params

    def clear(self):
        self.value = False
        self.function = ""
        self.params = ""

    def get(self):
        return self.value