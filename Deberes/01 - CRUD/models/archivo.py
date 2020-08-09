import json
import os

class Archivo:
    def __init__(self, ruta):
        self.ruta = ruta
        self.__leerArchivo()

    def __leerArchivo(self):
        if os.path.isfile(self.ruta):
            with open(self.ruta) as ruta:
                try:
                    self.contenido = json.load(ruta)
                except Exception:
                    print("El archivo esta vacio se creara uno nuevo")
                    self.contenido = []
        else:
            self.contenido = []
    
    def guardarArchivo(self):
        try:
            with open(self.ruta, "w") as ruta:
                json.dump(self.contenido, ruta)
        except Exception:
            print("No se pudo escribir en el archivo")
