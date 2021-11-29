from App.AppFrames.Controllers.Printers.TM_T88V import Printer
import inspect

def get_args(f):
        try:
            params = list(inspect.getfullargspec(f).args) # Python 3
        except AttributeError:
            params = list(inspect.getargspec(f).args)  # Python 2
        return params

class Api():
    def __init__(self):
        pass
    
    def hola_mundo(self, text):
        print(text)

api = Api()
functions = { name: get_args(getattr(api, name))[1:] for name in dir(api)
if inspect.ismethod(getattr(api, name)) and not name.startswith('_')}

functions = functions.items()
print([ {'func': name, 'params': params} for name, params in functions ])