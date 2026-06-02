from model.Guerrero import Guerrero
from model.Mago     import Mago
from model.Arquero  import Arquero

class Controlador:

    def __init__(self, vista, conexion):
        self.__vista    = vista
        self.__conexion = conexion

    # ── EJECUTAR ──────────────────────────────────────────────────────────────
    def ejecutar(self):
        op = -1
        while op != 0:
            op = self.__vista.mostrar_menu()
            if   op == 1: self.crear_personaje()
            elif op == 2: self.listar_personajes()    # ← NUEVO
            elif op == 3: self.buscar_por_nombre()    # ← busca por nombre
            elif op == 4: self.actualizar_nivel()     # ← NUEVO
            elif op == 5: self.eliminar_personaje()
            elif op == 6: self.combate()
            elif op == 0: self.__vista.mostrar_mensaje("¡Hasta luego!")
            else:         self.__vista.mostrar_mensaje("Opción no válida")

    # ── CREAR PERSONAJE ───────────────────────────────────────────────────────
    def crear_personaje(self):
        nombre = self.__vista.pedir_nombre()
        rol    = self.__vista.pedir_rol()

        if   rol == 1: p = Guerrero(nombre)
        elif rol == 2: p = Mago(nombre)
        elif rol == 3: p = Arquero(nombre)
        else:
            self.__vista.mostrar_mensaje("Rol inválido")
            return

        try:
            sql = """INSERT INTO personaje (nombre, rol, nivel, vida, daño, exp)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor = self.__conexion.get_conexion().cursor()
            cursor.execute(sql, (p.nombre, p.rol, p.nivel, p.vida, p.daño, p.exp))
            self.__conexion.get_conexion().commit()
            self.__vista.mostrar_mensaje(f"¡Personaje {p.nombre} creado!")
            self.__vista.mostrar_mensaje(p.habilidad_especial())
        except Exception as e:
            self.__vista.mostrar_mensaje(f"Error creando personaje: {e}")

    # ── LISTAR TODOS ──────────────────────────────────────────────────────────
    def listar_personajes(self):
        try:
            cursor = self.__conexion.get_conexion().cursor()
            cursor.execute("SELECT * FROM personaje")
            resultados = cursor.fetchall()  # trae TODOS los registros

            self.__vista.mostrar_mensaje("\n====== TODOS LOS PERSONAJES ======")
            if not resultados:
                self.__vista.mostrar_mensaje("No hay personajes registrados")
                return

            for r in resultados:  # recorre cada personaje
                self.__vista.mostrar_mensaje("─────────────────────────────────")
                self.__vista.mostrar_mensaje(f"ID:     {r[0]}")
                self.__vista.mostrar_mensaje(f"Nombre: {r[1]}")
                self.__vista.mostrar_mensaje(f"Rol:    {r[2]}")
                self.__vista.mostrar_mensaje(f"Nivel:  {r[3]}")
                self.__vista.mostrar_mensaje(f"Vida:   {r[4]}")
                self.__vista.mostrar_mensaje(f"Daño:   {r[5]}")
                self.__vista.mostrar_mensaje(f"Exp:    {r[6]}/100")

        except Exception as e:
            self.__vista.mostrar_mensaje(f"Error listando personajes: {e}")

    # ── BUSCAR POR NOMBRE ─────────────────────────────────────────────────────
    def buscar_por_nombre(self):
        nombre = self.__vista.pedir_nombre()

        try:
            sql    = "SELECT * FROM personaje WHERE nombre = %s"
            cursor = self.__conexion.get_conexion().cursor()
            cursor.execute(sql, (nombre,))
            r = cursor.fetchone()

            if r:
                self.__vista.mostrar_mensaje("\n====== PERSONAJE ENCONTRADO ======")
                self.__vista.mostrar_mensaje(f"ID:     {r[0]}")
                self.__vista.mostrar_mensaje(f"Nombre: {r[1]}")
                self.__vista.mostrar_mensaje(f"Rol:    {r[2]}")
                self.__vista.mostrar_mensaje(f"Nivel:  {r[3]}")
                self.__vista.mostrar_mensaje(f"Vida:   {r[4]}")
                self.__vista.mostrar_mensaje(f"Daño:   {r[5]}")
                self.__vista.mostrar_mensaje(f"Exp:    {r[6]}/100")
            else:
                self.__vista.mostrar_mensaje(f"No existe personaje con nombre: {nombre}")

        except Exception as e:
            self.__vista.mostrar_mensaje(f"Error buscando personaje: {e}")

    # ── ACTUALIZAR NIVEL ──────────────────────────────────────────────────────
    def actualizar_nivel(self):
        self.__vista.mostrar_mensaje("¿A qué personaje quieres subir el nivel?")
        id = self.__vista.pedir_id()

        try:
            # verifica que existe
            cursor = self.__conexion.get_conexion().cursor()
            cursor.execute("SELECT nombre FROM personaje WHERE id_personaje = %s", (id,))
            r = cursor.fetchone()

            if not r:
                self.__vista.mostrar_mensaje(f"No existe personaje con ID: {id}")
                return

            # UPDATE: sube nivel +1, vida +15, daño +20
            sql = """UPDATE personaje 
                     SET nivel = nivel + 1, vida = vida + 15, daño = daño + 20
                     WHERE id_personaje = %s"""
            cursor.execute(sql, (id,))
            self.__conexion.get_conexion().commit()

            self.__vista.mostrar_mensaje(f"¡{r[0]} subió de nivel!")
            self.__vista.mostrar_mensaje("Vida +15, Daño +20")

        except Exception as e:
            self.__vista.mostrar_mensaje(f"Error actualizando nivel: {e}")

    # ── ELIMINAR PERSONAJE ────────────────────────────────────────────────────
    def eliminar_personaje(self):
        id = self.__vista.pedir_id()

        try:
            sql    = "DELETE FROM personaje WHERE id_personaje = %s"
            cursor = self.__conexion.get_conexion().cursor()
            cursor.execute(sql, (id,))
            self.__conexion.get_conexion().commit()

            if cursor.rowcount > 0:
                self.__vista.mostrar_mensaje("Personaje eliminado exitosamente")
            else:
                self.__vista.mostrar_mensaje(f"No existe personaje con ID: {id}")

        except Exception as e:
            self.__vista.mostrar_mensaje(f"Error eliminando personaje: {e}")

    # ── COMBATE SIMULADO ──────────────────────────────────────────────────────
    def combate(self):
        self.__vista.mostrar_mensaje("¿Qué personaje va a combatir?")
        id = self.__vista.pedir_id()

        try:
            cursor = self.__conexion.get_conexion().cursor()
            cursor.execute("SELECT * FROM personaje WHERE id_personaje = %s", (id,))
            r = cursor.fetchone()

            if not r:
                self.__vista.mostrar_mensaje("Personaje no encontrado")
                return

            rol    = r[2]
            nombre = r[1]

            # POLIMORFISMO
            if   rol == "Guerrero": p = Guerrero(nombre)
            elif rol == "Mago":     p = Mago(nombre)
            else:                   p = Arquero(nombre)

            p.vida  = r[4]
            p.daño  = r[5]
            p.nivel = r[3]
            p.exp   = r[6]

            vida_mob = 45
            self.__vista.mostrar_mensaje("\n====== COMBATE INICIADO ======")
            self.__vista.mostrar_mensaje(f"MOB aparece con {vida_mob} de vida!")

            while vida_mob > 0:
                vida_mob -= 15
                self.__vista.mostrar_mensaje(
                    f"{p.nombre} ataca! MOB vida: {max(vida_mob, 0)}")

            self.__vista.mostrar_mensaje("¡MOB derrotado!")
            p.ganar_experiencia(15)

            sql = """UPDATE personaje 
                     SET nivel=%s, vida=%s, daño=%s, exp=%s
                     WHERE id_personaje=%s"""
            cursor.execute(sql, (p.nivel, p.vida, p.daño, p.exp, id))
            self.__conexion.get_conexion().commit()

            self.__vista.mostrar_mensaje(f"Exp actual: {p.exp}/100")
            self.__vista.mostrar_mensaje(f"Nivel actual: {p.nivel}")

        except Exception as e:
            self.__vista.mostrar_mensaje(f"Error en combate: {e}")
