from model.Personaje import Personaje

# HERENCIA: Mago ES UN Personaje
class Mago(Personaje):

    def __init__(self, nombre):
        # Mago es frágil pero poderoso: vida=80, daño=35
        super().__init__(nombre, 80, 35, "Mago")

    # POLIMORFISMO: su propia versión de habilidad_especial()
    def habilidad_especial(self):
        return f"{self.nombre} usa BOLA DE FUEGO y hace {self.daño * 2} de daño!"
