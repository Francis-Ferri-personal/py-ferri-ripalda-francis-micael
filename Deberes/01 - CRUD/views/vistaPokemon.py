from controllers.pokemonController import PokemonController

class VistaPokemon():
    def __init__(self):
        self.cargarConstantes()
        self.pokemonController = PokemonController()

    def interfaz(self):
        while True: 
            print(self.menu)
            opcion = input("Ingrese el numero -> ")
            if opcion in self.opciones:
                metodo = getattr(self, self.opciones[opcion])
                metodo()
            if opcion == "6":
                break

    def enviarCrearPokemon(self):
        pokemonParams = self.ingresarDatosPokemon()
        self.pokemonController.crearPokemon(pokemonParams)

    def enviarVerPokemon(self):
        idPokemon = int(input("Ingrese el ID del pokemon -> "))
        self.pokemonController.verPokemon(idPokemon)
        return idPokemon

    def enviarActualizarPokemon(self):
        idPokemon = self.enviarVerPokemon()
        pokemonParams = self.ingresarDatosPokemon()
        self.pokemonController.actualizarPokemon(idPokemon,pokemonParams)

    def enviarEliminarPokemon(self):
        idPokemon = int(input("Ingrese el ID del pokemon -> "))
        self.pokemonController.borrarPokemon(idPokemon)
        
    def enviarVerPokemons(self):
        self.pokemonController.verPokemones()

    def definirParametrosPokemon(self, nombre, tipo, subtipo, habitad, nivel, habilidades):
        pokemonParams = {
            "nombre": nombre,
            "tipo" : tipo,
            "subtipo" : subtipo,
            "habitad" : habitad,
            "nivel" :  nivel,
            "habilidades" : habilidades
        }
        return pokemonParams

    def ingresarDatosPokemon(self):
        nombre = input("Ingrese el nombre del pokemon -> ")
        tipo = input("Ingrese el tipo del pokemon -> ")
        subtipo = input("Ingrese el subtipo del pokemon -> ")
        habitad = input("Ingrese el habitad del pokemon -> ")
        nivel = int(input("Ingrese el nivel del pokemon -> "))
        habilidades = input("Ingrese las habilidades (separadas por \"-\") -> ")
        habilidades = habilidades.split("-")
        pokemonParams = self.definirParametrosPokemon(nombre, tipo, subtipo, habitad, nivel, habilidades)
        return pokemonParams

    def cargarConstantes(self):
        self.menu = f"""
                Escoja una opcion:
                1. Ingresar un nuevo pokemon
                2. Ver un pokemon
                3. Actualizar un pokemon
                4. Eliminar un pokemon
                5. Ver todos los pokemons
                6. Salir
            """
        self.opciones =  {
            "1": "enviarCrearPokemon",
            "2": "enviarVerPokemon",
            "3": "enviarActualizarPokemon",
            "4": "enviarEliminarPokemon",
            "5": "enviarVerPokemons"
        }