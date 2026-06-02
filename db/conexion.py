import mysql.connector  # pip install mysql-connector-python

# Puente entre Python y MySQL
# equivalente a Conexion.java
class Conexion:

    # datos de conexión
    __HOST     = "localhost"
    __USER     = "root"
    __PASSWORD = "sh3833"   # cambia por tu contraseña
    __DATABASE = "bd_multi"

    def __init__(self):
        self.__conexion = None

    # abre el puente con MySQL
    def get_conexion(self):
        try:
            self.__conexion = mysql.connector.connect(
                host     = self.__HOST,
                user     = self.__USER,
                password = self.__PASSWORD,
                database = self.__DATABASE
            )
        except Exception as e:
            print(f"Error conectando a MySQL: {e}")
        return self.__conexion

    # cierra el puente
    def cerrar(self):
        if self.__conexion:
            self.__conexion.close()
