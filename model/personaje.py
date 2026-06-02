
from abc import ABC, abstractmethod  # ABC = clase abstracta en Python

# abstract en Python se hace con ABC y @abstractmethod
class Personaje(ABC):

    # Constructor — __init__ es el equivalente al constructor de Java
    def __init__(self, nombre, vida, daño, rol):
        self.__id     = None   # lo genera MySQL con AUTO_INCREMENT
        self.__nombre = nombre
        self.__vida   = vida
        self.__daño   = daño
        self.__rol    = rol
        self.__nivel  = 1      # siempre arranca en 1
        self.__exp    = 0      # siempre arranca en 0

    # ── LÓGICA DE EXPERIENCIA ─────────────────────────────────────────────────
    def ganar_experiencia(self, cantidad):
        self.__exp += cantidad
        if self.__exp >= 100:          # condición para subir de nivel
            self.__nivel += 1
            self.__vida  += 15
            self.__daño  += 20
            self.__exp    = 0
            print(f"¡{self.__nombre} subió al nivel {self.__nivel}!")

    # ── MÉTODO ABSTRACTO ──────────────────────────────────────────────────────
    # equivalente a "public abstract String habilidadEspecial()" en Java
    # las hijas DEBEN implementarlo o Python lanza error
    @abstractmethod
    def habilidad_especial(self):
        pass

    # ── GETTERS (@property = equivalente a getNombre() en Java) ───────────────
    @property
    def id(self):       return self.__id
    @property
    def nombre(self):   return self.__nombre
    @property
    def vida(self):     return self.__vida
    @property
    def daño(self):     return self.__daño
    @property
    def nivel(self):    return self.__nivel
    @property
    def exp(self):      return self.__exp
    @property
    def rol(self):      return self.__rol

    # ── SETTERS (@property.setter = equivalente a setNombre() en Java) ────────
    @id.setter
    def id(self, valor):
        self.__id = valor

    @vida.setter
    def vida(self, valor):
        if valor < 0: valor = 0   # la vida nunca puede ser negativa
        self.__vida = valor

    @daño.setter
    def daño(self, valor):
        if valor < 0: return      # el daño nunca puede ser negativo
        self.__daño = valor

    @nivel.setter
    def nivel(self, valor):
        if valor < 1: return      # el nivel nunca puede ser menor a 1
        self.__nivel = valor

    @exp.setter
    def exp(self, valor):
        if valor < 0: return      # la exp nunca puede ser negativa
        self.__exp = valor
