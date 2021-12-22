import sys
import logging
from App import Player
from App import Configuration

logging.basicConfig(filename="log.log", level=logging.DEBUG, format=("%(asctime)s:%(levelname)s:%(message)s"), datefmt="%m/%d/%Y %I:%M:%S %p")

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