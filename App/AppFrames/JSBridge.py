import json
import inspect


class JSBridge:
    """
    Clase que permite la interaccipn entre la url y la aplicacion local
    :param browser: cef browser, nevegador donde se corre la url
    :param api: dic. informacion del nombre y objeto de los controladores
    """

    def __init__(self, browser, api):
        """
        Constructor de clase
        :param browser: cef browser, nevegador donde se corre la url
        :param api: dic. informacion del nombre y objeto de los controladores
        """
        self.browser = browser
        self.api = api
        

    def parse_api_js(self):
        """
        Carga la api en el navegador
        """
        def get_args(func):
            """
            Devuelve la lista de los argumentos de una funcion
            :param func: funct. funcion a extraer los argumentos
            :return: list. argumentos de la funcion
            """
            return list(inspect.getfullargspec(func).args)
        
        def generate_func():
            """
            Genera la api y las funciones que seran llamadas en el navegador
            :return: str. codigo JavaScript que sera ejecutado por el navegador (carga de funciones)
            """
            functions = {}
            for controllerName, controller in self.api.items():
                methods = {}
                for name in dir(controller):
                    if inspect.ismethod(getattr(controller, name)) and not name.startswith('_'):    
                        methods[name] = get_args(getattr(controller, name))[1:]
                functions[controllerName] = methods
            funs = []
            for controller, methods in functions.items():
                method = [{"func": name, "params":params} for name, params in methods.items()]
                funs.append({"controller": controller, "methods":method})
            js = """window.api = {
                        _createApi: function(controllerList){
                        for(var i = 0; i < controllerList.length; i++){
                            var methodList = controllerList[i].methods;
                            var controller = controllerList[i].controller; 
                            window.api[controller] = {}; 
                            window.api.returnValues[controller] = {}; 
                            for(var j = 0; j < methodList.length; j++){
                            var funcName = methodList[j].func; 
                            var params = methodList[j].params;
                            var funcBody = 
                                "var id = (Math.random()+'').substring(2);"+
                                "var promise = new Promise(function(resolve, reject){"+
                                    "window.api._checkValue('"+funcName+"', '"+controller+"',resolve, reject, id);"+
                                "});"+
                                "window.api._bridge.call('"+funcName+"', '"+controller+"', arguments, id);"+
                                "return promise"
                                
                                window.api[controller][funcName] = new Function(params, funcBody)
                                window.api.returnValues[controller][funcName] = {}
                            };
                        };
                    },
                _bridge:{
                        call: function (funcName, controller , params, id){
                            return window.external.call(funcName, controller, JSON.stringify(params), id);
                        }
                    },
                _checkValue: function(funcName, controller, resolve, reject, id){
                        var check = setInterval(function(){
                            var returnObj = window.api.returnValues[controller][funcName][id];
                            if(returnObj){
                                var value = returnObj.value;
                                var isError = returnObj.isError;

                                delete window.api.returnValues[controller][funcName][id];
                                clearInterval(check);
                                
                                if (isError){
                                    var pyError = JSON.parse(value);
                                    var error = new Error(pyError.message);
                                    
                                    reject(error);
                                } else {
                                    resolve(JSON.parse(value));
                                }
                            }
                        }, 100)
                    }, 
                    returnValues: {}
            }
            try{
                window.api._createApi(%s);
            }catch (error){
                document.getElementById("paper_state").innerHTML = error;
            }
            """
            return js % funs
        return generate_func()

    def call(self, func_name, controller, param, id):
        """
        Llama a las funciones de los controladores y guarda los retornos o errores en un objeto del navegador
        :param func_name: str. nombre de la funcion a llamar
        :param controller: str. nombre del controlador donde se encuentra la funcion
        :param param: dic. parametros que seran enviados a la funcion
        :param id: int. identificacion del llamado de la funcion
        """
        def _call():
            try:
                result = func(*func_params.values())    
                result = json.dumps(result).replace('\\', '\\\\').replace('\'', '\\\'')
                code = 'window.api.returnValues["{0}"]["{1}"]["{2}"] = {{value:\'{3}\'}}'.format(controller, func_name, id, result)
                
            except Exception as e :
                error = {
                    "message": str(e),
                }
                result = json.dumps(error).replace('\\', '\\\\').replace('\'', '\\\'')
                code = 'window.api.returnValues["{0}"]["{1}"]["{2}"] = {{isError: true, value:\'{3}\'}}'.format(controller, func_name, id, result)
            self.browser.ExecuteJavascript(code)
        func = getattr(self.api[controller], func_name, None)
        
        if func is not None:
            func_params = json.loads(param)
            _call()
        else:
            raise Exception("La funcion no existe")
        
