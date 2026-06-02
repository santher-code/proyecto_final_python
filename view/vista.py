class Vista:

    def mostrar_menu(self):
        print("\n====== RPG MANAGER ======")
        print("1. Crear personaje")
        print("2. Listar todos los personajes")
        print("3. Buscar personaje por nombre")
        print("4. Actualizar nivel")
        print("5. Eliminar personaje")
        print("6. Combate simulado")
        print("0. Salir")
        return int(input("Elige una opción: "))

    def pedir_rol(self):
        print("Elige tu rol:")
        print("1. Guerrero (vida: 120, daño: 25)")
        print("2. Mago     (vida: 80,  daño: 35)")
        print("3. Arquero  (vida: 100, daño: 20)")
        return int(input("Rol: "))

    def pedir_nombre(self):
        return input("Digite el nombre del personaje: ")

    def pedir_id(self):
        return int(input("Digite el ID del personaje: "))

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
