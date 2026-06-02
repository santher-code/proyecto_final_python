from model.Personaje import Personaje

# HERENCIA: Guerrero(Personaje) = equivalente a "extends Personaje" en Java
class Guerrero(Personaje):

    def __init__(self, nombre):
        # super().__init__() = equivalente a super() en Java
        super().__init__(nombre, 120, 25, "Guerrero")

    # POLIMORFISMO: reemplaza el método abstracto del padre
    # no necesita @Override, Python lo hace automáticamente
    def habilidad_especial(self):
        return f"{self.nombre} usa CORTE SUPREMO y hace {self.daño * 2} de daño!"
