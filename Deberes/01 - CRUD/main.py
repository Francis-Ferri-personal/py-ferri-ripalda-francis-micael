from views.vistaPokemon import VistaPokemon
from views.vistaEntrenador import VistaEntrenador

menu = f"""
    Escoja una opcion:
    1. Gestionar entrenadores
    2. Gestionar pokemons
    3. Salir
"""

def iniciarVistaEntrenador():
    vistaEntrenador = VistaEntrenador()
    vistaEntrenador.interfaz()

def iniciarVistaPokemon():
    vistaPokemon = VistaPokemon()
    vistaPokemon.interfaz()

opciones =  {
    "1": iniciarVistaEntrenador,
    "2": iniciarVistaPokemon,
}

while True:
    print(menu)
    opcion = input("Ingrese el numero -> ")
    if opcion in opciones:
        metodo = opciones.get(opcion)
        metodo()
    if opcion == "3":
        break

"""
Cosas extras que se podria agregar

tiposPokemon =  ("Normal", "Lucha", "Volador", "Veneno", "Tierra", "Roca", "Bicho", "Fantasma", "Acero", "Fuego", "Agua", "Planta", "Eléctrico", "Psíquico", "Hielo", "Dragón", "Hada", "Siniestro")

medallasPokemon = ("Medalla roca", "Medalla cascada", "Medalla Trueno"," Medalla Arcoiris", "Medalla Alma", "Medalla Pantano")

regiones = ("Kanto", "Johto", "Hoenn", "Sinnoh", "Teselia", "Kalos", "Alola", "Galar",  "Aura", "Floresta", "Almia", "Oblivia", "Sol", "Ransei", "Ferrum")

habilidades = ("Cola de hierro", "Impactrueno", "Sacudida", "Orejaso", "Impulso",  "Armadura batalla", "Despiste", "Intimidación","Sombra trampa", "Pararrayos")
"""