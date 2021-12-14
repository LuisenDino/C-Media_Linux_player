from ..Connection.SerialConnection import SerialConnection
import threading
import logging

class BarCodeReader():
    def __init__(self, device):
        
        self.device = device
        self.result = None
        self.reader = None
        self.thread = None
        self.killThread = False

        self.connect()
        #Constructor
        self.detalle = "Manejo de puerto serial"

    def get_result(self):
        return self.result

    def connect(self):
        
        try:
            self.reader = SerialConnection(self.device["port"]) #/dev/ttyACM0
        except Exception as e:
            logging.error(str(e))
            print(str(e))
            return str(e)
        
        if(self.thread == None):
            self.thread = threading.Thread(target=self.receiveData)
            self.thread.start()
            
        
    def receiveData(self):
        while not self.killThread:
            
            try:
                b = self.reader.read() 
            except Exception as e:
                print(str(e))
            if(self.killThread):
                break
            byte = bytearray()
            while  b != b"\r" and not self.killThread:
                byte+=b
                b = self.reader.read()
            self.procesar_datos(byte[0], byte[1:])
            

    def procesar_datos(self, prefix, byte):
        if(prefix != 114):
            self.result = byte.decode("utf-8")
        else:
            cedula = {}
            if(byte[32:34] == b"CE"):
                cedula["TipoDocumento"] = "CedulaExtrangeria"
                b=34
                cedula_byte = bytearray()
                while (byte[b] < 0x3A and byte[b] > 0x2F):
                    cedula_byte.append(byte[b])
                    b+=1
                cedula["NumeroCedula"] = cedula_byte.decode('utf-8').replace('\0', "").lstrip("0")
                primer_apellido = bytearray()
                for i in range(30):
                    primer_apellido.append(byte[i+52])
                cedula["PrimerApellido"] = self.replaces(primer_apellido)
                
                segundo_apellido = bytearray()
                for i in range(30):
                    segundo_apellido.append(byte[i+82])
                cedula["SegundoApellido"] = self.replaces(segundo_apellido)

                primer_nombre = bytearray()
                segundo_nombre = bytearray()
                b = 0
                while byte[b+112] != 0x20:
                    primer_nombre.append(b+112)
                    b+=1
                
                while byte[b + 112] != 0:
                    segundo_nombre.append(b+112)
                    b+=1
                
                cedula["PrimerNombre"] = self.replaces(primer_nombre)

                cedula["SegundoNombre"] = self.replaces(segundo_nombre)
                
                cedula["Sexo"] = chr(byte[200])

                cumpleanos = bytearray()
                for i in range(8):
                    cumpleanos.append(byte[i+192])
                cedula["FechaDeNacimiento"] = cumpleanos.decode('utf-8')

                sangre = bytearray()
                for i in range(2):
                    sangre.append(byte[i+217])
                cedula["RH"] = sangre.decode('utf-8')

                pais = bytearray()
                for i in range(30):
                    pais.append(byte[i+220])

                cedula["Pais"] = self.replaces(pais)    


                department = bytearray()
                for i in range(2):
                    department.append(byte[i+160])
                
                cedula["Departamento"] = department.decode('utf-8')
                cedula["Departamento"] = cedula["Departamento"].replace("\0", "")

                city = bytearray() 
                for i in range(3):
                    city.append(byte[i+162])
                
                cedula["Ciudad"] = city.decode('utf-8')
                cedula["Ciudad"] = cedula["Ciudad"].replace("\0", "")
            elif(byte[0] == ord("I")):
                cedula["TipoDocumento"] = "TaretaIdentidad"
                cedula_byte = bytearray()
                if(byte[48] == ord('0') and byte[49] == ord('0')):
                    b = 50
                    while byte[b] < 0x3A and byte[b] > 0x2F:
                        cedula_byte.append(byte[b])
                        b+=1
                else:
                    b = 48
                    while byte[b] <0x3A and byte[b] > 0x2F:
                        cedula_byte.append(byte[b])
                        b+=1
                    tempOffset = b
                cedula["NumeroCedula"] = cedula_byte.decode('utf-8')
                
                primer_apellido = bytearray()
                for i in range(23):
                    primer_apellido.append(byte[i+tempOffset])

                cedula["PrimerApellido"] = self.replaces(primer_apellido)

                segundo_apellido = bytearray()
                for i in range(23):
                    segundo_apellido.append(byte[i+81])

                cedula["SegundoApellido"] = self.replaces(segundo_apellido)

                primer_nombre = bytearray()
                for i in range(23):
                    primer_nombre.append(byte[i+104])

                cedula["PrimerNombre"] = self.replaces(primer_nombre)
                
                segundo_nombre = bytearray()
                for i in range(23):
                    segundo_nombre.append(byte[i+127])
                
                cedula["SegundoNombre"] = self.replaces(segundo_nombre)
                
                cedula["Sexo"] = chr(byte[152])

                cumpleanos = bytearray()
                for i in range(8):
                    cumpleanos.append(byte[i+153])

                cedula["FechaDeNacimiento"] = cumpleanos.decode('utf-8')

                sangre = bytearray()
                for i in range(2):
                    sangre.append(byte[i+167])
                
                cedula["RH"] = sangre.decode('utf-8')

                department = bytearray()
                for i in range(2):
                    department.append(byte[i+161])

                cedula["Departamento"] = department.decode('utf-8')

                city = bytearray()
                for i in range(3):
                    city.append(byte[i+163])

                cedula["Ciudad"] = city.decode('utf-8')

                cedula["Pais"] = "COL"
            else:
                cedula["TipoDocumento"] = "CedulaCiudadania"
                cedula_byte = bytearray()
                if(byte[48] == ord('0') and byte[49] == ord('0')):
                    b = 50
                    while byte[b] < 0x3A and byte[b] > 0x2F:
                        cedula_byte.append(byte[b])
                        b+=1
                else:
                    b = 48
                    while byte[b] <0x3A and byte[b] > 0x2F:
                        cedula_byte.append(byte[b])
                        b+=1
                cedula["NumeroCedula"] = cedula_byte.decode('utf-8')
                
                primer_apellido = bytearray()
                for i in range(23):
                    primer_apellido.append(byte[i+58])

                cedula["PrimerApellido"] = self.replaces(primer_apellido)

                segundo_apellido = bytearray()
                for i in range(23):
                    segundo_apellido.append(byte[i+81])

                cedula["SegundoApellido"] = self.replaces(segundo_apellido)

                primer_nombre = bytearray()
                for i in range(23):
                    primer_nombre.append(byte[i+104])

                cedula["PrimerNombre"] = self.replaces(primer_nombre)
                
                segundo_nombre = bytearray()
                for i in range(23):
                    segundo_nombre.append(byte[i+127])
                
                cedula["SegundoNombre"] = self.replaces(segundo_nombre)
                
                cedula["Sexo"] = chr(byte[151])

                cumpleanos = bytearray()
                for i in range(8):
                    cumpleanos.append(byte[i+152])

                cedula["FechaDeNacimiento"] = cumpleanos.decode('utf-8')

                sangre = bytearray()
                for i in range(2):
                    sangre.append(byte[i+166])
                
                cedula["RH"] = sangre.decode('utf-8')

                department = bytearray()
                for i in range(2):
                    department.append(byte[i+160])

                cedula["Departamento"] = department.decode('utf-8')

                city = bytearray()
                for i in range(3):
                    city.append(byte[i+162])

                cedula["Ciudad"] = city.decode('utf-8')

                cedula["Pais"] = "COL"
            self.result = cedula
            return cedula
            

    def replaces(self, byte):
        for i in range(len(byte)):
            if byte[i] == 209: 
                byte[i]='Ñ'.encode("utf-8")
        string = byte.decode("utf-8")
        if "\0" in string:
            string = string.replace("\0", "")
        elif " " in string:
            string = string.replace(" ", "")
        if "?" in string:
            string = string.replace("?", "Ñ")
        return string

    def disconnect (self):
        self.killThread = True
        self.reader.device.cancel_read()
        self.thread.join()
        
    def clear_result(self):
        self.result = None

