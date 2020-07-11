from models.pokemon import Pokemon
from models.archivo import Archivo
import data.constantes as const

class PokemonController():
    def __init__(self):
        self.rutaArchivo =  const.POKEMONS_FILE
        self.archivo = Archivo(self.rutaArchivo)
        self.listaPokemons = []
        self.listaEstructuraPokemons = []
        self.__cargarPokemons()       
    
    def __cargarPokemons(self):
        self.listaEstructuraPokemons = self.archivo.contenido
        for pokemonParams in self.listaEstructuraPokemons:
            pokemon = self.__nuevoPokemon(pokemonParams["id"], pokemonParams)
            self.listaPokemons.append(pokemon)

    def __nuevoPokemon(self, id, pokemonParams):
        pokemon = Pokemon(
            id,
            pokemonParams["nombre"],
            pokemonParams["tipo"],
            pokemonParams["subtipo"],
            pokemonParams["habitad"],
            pokemonParams["nivel"],
            pokemonParams["habilidades"]
        )
        return pokemon

    def __pokemonEstructura(self, pokemon):
        return {
            "id" : pokemon.id,
            "nombre" : pokemon.nombre,
            "tipo" : pokemon.tipo,
            "subtipo" : pokemon.subtipo,
            "habitad" : pokemon.habitad,
            "nivel" : pokemon.nivel,
            "habilidades" : pokemon.habilidades
        }

    def crearPokemon(self, pokemonParams):
        id = len(self.listaPokemons)
        pokemon = self.__nuevoPokemon(id, pokemonParams)
        pokemonEstructura = self.__pokemonEstructura(pokemon)
        self.listaPokemons.append(pokemon)
        self.listaEstructuraPokemons.append(pokemonEstructura)
        self.archivo.guardarArchivo()
        print(pokemon)
        return id

    def verPokemon(self, idPokemon):
        for pokemon in self.listaPokemons:
            if pokemon.id == idPokemon:
                print(pokemon)
                break

    def actualizarPokemon(self, idPokemon, pokemonParams):
        pokemon = self.listaPokemons[idPokemon]
        pokemon.nombre = pokemonParams["nombre"]
        pokemon.tipo = pokemonParams["tipo"]
        pokemon.subtipo = pokemonParams["subtipo"]
        pokemon.habitad = pokemonParams["habitad"]
        pokemon.nivel = pokemonParams["nivel"]
        pokemon.habilidades = pokemonParams["habilidades"]
        pokemonEstructura = self.__pokemonEstructura(pokemon)
        self.listaEstructuraPokemons[idPokemon] = pokemonEstructura
        self.archivo.guardarArchivo()
        print(pokemon)
                
    def borrarPokemon(self, idPokemon):
        print("Pokemon a eliminar")
        self.verPokemon(idPokemon)
        self.listaEstructuraPokemons.pop(idPokemon)
        self.listaPokemons.pop(idPokemon)
        self.archivo.guardarArchivo()
        print("Se eliminó el Pokemon")

    def verPokemones(self):
        listaImpresa = ""
        for pokemon in self.listaPokemons:
            listaImpresa += f" | ID: {pokemon.id} | Nombre: {pokemon.nombre} | Nivel: {pokemon.nivel} |\n"
        print(listaImpresa)

