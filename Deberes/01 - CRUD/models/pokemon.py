class Pokemon:
    def __init__(self, id, nombre, tipo, subtipo, habitad, nivel, habilidades):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.subtipo = subtipo
        self.habitad = habitad
        self.nivel = nivel
        self.habilidades = habilidades
        
    def __str__(self):
        return f"""
            ID: {self.id}
            Nombre del Pokemon: {self.nombre}
            Tipos: {self.tipo} {self.subtipo}
            Habitad: {self.habitad}
            Habilidades: {self.habilidades}
            Nivel: {self.nivel}
        """