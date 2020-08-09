from controllers.entrenadorController import EntrenadorController

class VistaEntrenador:
    def __init__(self):
        self.cargarConstantes()
        self.entrenadorController = EntrenadorController()

    def interfaz(self):
        while True: 
            print(self.menu)
            opcion = input("Ingrese el numero -> ")
            if opcion in self.opciones:
                metodo = getattr(self,self.opciones[opcion])
                metodo()
            if opcion == "6":
                break

    def enviarCrearEntrenador(self):
        # TODO Programar interaccion
        entrenadorParams = self.ingresarDatosEntrenador()
        self.entrenadorController.crearEntrenador(entrenadorParams)

    def enviarVerEntrenador(self):
        idEntrenador = int(input("Ingrese el ID del entrenador -> "))
        self.entrenadorController.verEntrenador(idEntrenador)
        return idEntrenador

    def enviarActualizarEntrenador(self):
        idEntrenador = self.enviarVerEntrenador()
        entrenadorParams = self.ingresarDatosEntrenador()
        self.entrenadorController.actualizarEntrenador(idEntrenador, entrenadorParams)

    def enviarEliminarEntrenador(self):
        idEntrenador = int(input("Ingrese el ID del entrenador -> "))
        self.entrenadorController.borrarEntrenador(idEntrenador)
    
    def enviarVerEntrenadores(self):
        self.entrenadorController.verEntrenadores()
    
    def ingresarDatosEntrenador(self):
        nombre = input("Ingrese el nombre del entrenador -> ")
        region = input("Ingrese la region del entrenador -> ")
        nivel = input("Ingrese el nivel del entrenador -> ")
        pokemons = input("Ingrese los IDs de los pokemons (separadas por \"-\") -> ")
        medallas = input("Ingrese las medallas (separadas por \"-\") -> ")
        pokemons = pokemons.split("-")
        medallas = medallas.split("-")
        entrenadorParams = self.definirParametrosEntrenador(nombre, region, nivel, pokemons, medallas)
        return entrenadorParams

    def definirParametrosEntrenador(self, nombre, region, nivel, pokemons, medallas):
        entrenadorParams = {
            "nombre": nombre,
            "region" : region,
            "nivel" : nivel,
            "pokemons" : pokemons,
            "medallas" :  medallas,
        }
        return entrenadorParams
    
    def cargarConstantes(self):
        self.menu = f"""
                Escoja una opcion:
                1. Ingresar un nuevo entrenador
                2. Ver un entrenador
                3. Actualizar un entrenador
                4. Eliminar un entrenador
                5. Ver todos los entrenadores
                6. Salir
            """
        self.opciones =  {
            "1": "enviarCrearEntrenador",
            "2": "enviarVerEntrenador",
            "3": "enviarActualizarEntrenador",
            "4": "enviarEliminarEntrenador",
            "5": "enviarVerEntrenadores"
        }