import sys
import logging
#import Player
#import Configuration
from App import Player
from App import Configuration
import os
import tkinter as tk
from screeninfo import get_monitors

logging.basicConfig(filename=os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/logs/log.log", level=logging.DEBUG, format=("%(asctime)s:%(levelname)s:%(message)s"), datefmt="%m/%d/%Y %I:%M:%S %p")

splash_root = tk.Tk(className="C-Media Player")

splash_root.title("C-Media")

image = tk.PhotoImage(file=os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/LOGO-CMedia.png")
splash_root.tk.call('wm', 'iconphoto', splash_root._w, image)
monitors = get_monitors()
for monitor in monitors:
    if monitor.is_primary:
        h=250
        w=402
        splash_root.geometry(str(w)+"x"+str(h)+"+"+str(monitor.width//2-w//2)+"+"+str(monitor.height//2-h//2)) 
splash_root.configure(background="#f3f3f3")
#splash_root.configure(background="#0a3749")

img = tk.PhotoImage(file=os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/SplashScreen.png")
#tk.Label(splash_root, image=img, bg="#0a3749").pack(fill=tk.BOTH, expand=True)
tk.Label(splash_root, image=img, bg="#f3f3f3").pack(fill=tk.BOTH, expand=True)
splash_root.overrideredirect(True)

def call_app():
    if len(sys.argv) == 1:
        try:
            Player.main(splash_root)
        except Exception as e:
            logging.error(str(e))
    elif "--config" in sys.argv:
        try:
            Configuration.main(splash_root)
        except Exception as e:
            logging.error(str(e))
    else:
        logging.error("Opcion no permitida")
    

splash_root.after(2000, call_app)
splash_root.mainloop()