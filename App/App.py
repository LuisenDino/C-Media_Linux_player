import sys
import logging
#import Player
#import Configuration
from App import Player
from App import Configuration
import os

logging.basicConfig(filename=os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/logs/log.log", level=logging.DEBUG, format=("%(asctime)s:%(levelname)s:%(message)s"), datefmt="%m/%d/%Y %I:%M:%S %p")

if len(sys.argv) == 1:
    try:
        Player.main()
    except Exception as e:
        logging.error(str(e))
elif "--config" in sys.argv:
    try:
        Configuration.main()
    except Exception as e:
        logging.error(str(e))
else:
    logging.error("Opcion no permitida")