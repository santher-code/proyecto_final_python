from view.Vista          import Vista
from db.Conexion         import Conexion
from controller.Controlador import Controlador

# Punto de entrada del programa
# equivalente a Main.java
if __name__ == "__main__":

    # 1. crea la Vista
    vista = Vista()

    # 2. crea la Conexion con MySQL
    conexion = Conexion()

    # 3. crea el Controlador — sin "new", Python no lo necesita
    controlador = Controlador(vista, conexion)

    # 4. arranca el programa
    controlador.ejecutar()

    # 5. cierra la conexión al salir
    conexion.cerrar()
