from model.Personaje import Personaje

# HERENCIA: Arquero ES UN Personaje
class Arquero(Personaje):

    def __init__(self, nombre):
        # Arquero equilibrado: vida=100, daño=20
        super().__init__(nombre, 100, 20, "Arquero")

    # POLIMORFISMO: su propia versión de habilidad_especial()
    def habilidad_especial(self):
        return f"{self.nombre} usa FLECHA DIVINA y hace {self.daño * 2} de daño!"
