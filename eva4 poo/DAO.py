import mysql.connector
import Credenciales
from Curso import Curso

class DAO:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None
    
    def conectar(self):
        self.__conexion = mysql.connector.connect(**Credenciales.get_credenciales())
        self.__cursor = self.__conexion.cursor()
        
    def cerrar(self):
        self.__conexion.commit()
        self.__conexion.close()
    
    def registrarCurso(self, c: Curso):
        self.conectar()
        sql = "INSERT INTO 6svcurso (nombre, sala, valor, docente, tamano_sala, seccion, duracion, disponibilidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (c.get_nombre(), c.get_sala(), c.get_valor(), c.get_docente(), c.get_tamano_sala(), c.get_seccion(), c.get_duracion(), c.get_disponibilidad())
        self.__cursor.execute(sql, values)
        self.cerrar()
