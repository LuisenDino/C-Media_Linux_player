import serial #libreria que permite la conexion con puerto serial
import logging #libreria de logging

class SerialConnection():
    """
    clase de coneccion a los dispositivos conectados por puerto serial.
    :param port: string. Ubicacion del archivo del puerto
    :param timeout: int. Opcional. Limite de tiempo.
    :param baudrate: tasa de baudios.
    """
    def __init__(self, port, timeout = 2000, baudrate = 9600):
        """
        La funcion es el constructor de la clase UsbConnection.
        :param port: string. Ubicacion del archivo del puerto
        :param timeout: int. Opcional. Limite de tiempo.
        :param baudrate: tasa de baudios.
        """
        self.port = port
        self.timeout = timeout
        self.baudrate = baudrate
        self.connect()



    def connect(self):
        """
        La funcion realiza la coneccion del objeto con el dispositivo mediante el puerto USB
        :return: str. Error
        """
        try:
            self.device = serial.Serial(self.port, timeout = self.timeout, baudrate = self.baudrate)
        except Exception as e:
            logging.error(str(e))
            return str(e)

    def write(self, data):
        """
        La funcion escribe un conjunto de bytes en el puerto USB.
        :param data: bytearray. Conjunto de bytes a escribir en el puertp USB.
        """
        try:
            self.device.write(data)
        except Exception as e:
            logging.error(str(e))
            return str(e)

    def read(self):
        """
        La funcion lee una cantidad de bytes del puerto USB.
        :return: array. Conjunto de bytes con informacion leidos en el puerto USB. 
        """
        try:
            return self.device.read()
        except Exception as e:
            logging.error(str(e))
            return str(e)

    def read_line(self):
        """
        La funcion lee una cantidad de bytes del puerto USB.
        :return: array. Conjunto de bytes con informacion leidos en el puerto USB. 
        """
        try:
            return self.device.readline()
        except Exception as e:
            logging.error(str(e))
            return str(e)

    def diconnect(self):
        """
        La funcion cierra la conexion con el puerto serial
        """
        try:
            self.device.close()
        except Exception as e:
            logging.error(str(e))
            return str(e)