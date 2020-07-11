class Entrenador:
    def __init__(self, id, nombre, region, nivel, pokemons, medallas):
        self.id = id
        self.nombre = nombre
        self.region = region
        self.nivel = nivel
        self.pokemons = pokemons
        self.medallas = medallas
        
    def __str__(self):
        return f"""
            ID: {self.id}
            Nombre del Pokemon: {self.nombre}
            Region: {self.region}
            Nivel: {self.nivel}
            Medallas: {self.medallas}
        """