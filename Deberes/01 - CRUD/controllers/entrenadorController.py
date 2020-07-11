from models.entrenador import Entrenador
from models.archivo import Archivo
import data.constantes as const
from controllers.pokemonController import PokemonController

class EntrenadorController:
    def __init__(self):
        self.rutaArchivo = const.ENTRENADORES_FILE
        self.archivo = Archivo(self.rutaArchivo)
        self.pokemonController = PokemonController()
        self.listaEntrenadores = []
        self.listaEstructuraEntrenadores = []
        self.__cargarEntrenadores()

    def __cargarEntrenadores(self):
        self.listaEstructuraEntrenadores = self.archivo.contenido
        for entrenadorParams in self.listaEstructuraEntrenadores:
            entrenador = self.__nuevoEntrenador(entrenadorParams["id"], entrenadorParams)
            self.listaEntrenadores.append(entrenador)

    def __nuevoEntrenador(self, id, entrenadorParams):
        entrenador = Entrenador(
            id,
            entrenadorParams["nombre"],
            entrenadorParams["region"],
            entrenadorParams["nivel"],
            entrenadorParams["pokemons"],
            entrenadorParams["medallas"]
        )
        return entrenador  

    def __entrenadorEstructura(self, entrenador):
        return {
            "id" : entrenador.id,
            "nombre" : entrenador.nombre,
            "region" : entrenador.region,
            "nivel" : entrenador.nivel,
            "pokemons" : entrenador.pokemons,
            "medallas" : entrenador.medallas
        }
    
    def crearEntrenador(self, entrenadorParams):
        id = len(self.listaEntrenadores)
        entrenador = self.__nuevoEntrenador(id, entrenadorParams)
        entrenadorEstructura = self.__entrenadorEstructura(entrenador)
        self.listaEntrenadores.append(entrenador)
        self.listaEstructuraEntrenadores.append(entrenadorEstructura)
        self.archivo.guardarArchivo()
        print(entrenador)
        self.imprimirPokemonsEntrenador(entrenador.pokemons)

    def verEntrenador(self, idEntrenador):
        for entrenador in self.listaEntrenadores:
            if entrenador.id == idEntrenador:
                print(entrenador)
                self.imprimirPokemonsEntrenador(entrenador.pokemons)
        
    def actualizarEntrenador(self, idEntrenador, entrenadorParams):
        entrenador = self.listaEntrenadores[idEntrenador]
        entrenador.nombre = entrenadorParams["nombre"]
        entrenador.region = entrenadorParams["region"]
        entrenador.nivel = entrenadorParams["nivel"]
        entrenador.pokemons = entrenadorParams["pokemons"]
        entrenador.medallas = entrenadorParams["medallas"]
        entrenadorEstructura = self.__entrenadorEstructura(entrenador)
        self.listaEstructuraEntrenadores[idEntrenador] = entrenadorEstructura
        self.archivo.guardarArchivo()
        print(entrenador)
        self.imprimirPokemonsEntrenador(entrenador.pokemons)

    def borrarEntrenador(self, idEntrenador):
        idsPokemons = self.listaEntrenadores[idEntrenador].pokemons
        print("Entrenador a eliminar")
        self.verEntrenador(idEntrenador)
        self.imprimirPokemonsEntrenador(idsPokemons)
        self.listaEstructuraEntrenadores.pop(idEntrenador)
        self.listaEntrenadores.pop(idEntrenador)
        self.archivo.guardarArchivo()
        print("Se eliminó el Entrenador")

    def verEntrenadores(self):
        listaImpresa = ""
        for entrenador in self.listaEntrenadores:
            listaImpresa += f" | ID: {entrenador.id} | Nombre: {entrenador.nombre} | Nivel: {entrenador.nivel} |\n"
        print(listaImpresa)

    def imprimirPokemonsEntrenador(self, idsPokemons):
        print("Pokemons del entrenador:")
        for idPokemon in idsPokemons:
            self.pokemonController.verPokemon(int(idPokemon))
