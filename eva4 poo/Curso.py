class Curso:
    def __init__(self, nombre, sala, valor, docente, tamano_sala, seccion, duracion, disponibilidad, id6svcurso):
        self.__nombre = nombre
        self.__sala = sala
        self.__valor = valor
        self.__docente = docente
        self.__tamano_sala = tamano_sala
        self.__seccion = seccion
        self.__duracion = duracion
        self.__disponibilidad = disponibilidad
        self.__id6svcurso = id6svcurso

    def get_id6svcurso(self):
      return self.__id6svcurso
    def set_id6svcurso(self,id6svcurso):
      self.__id6svcurso = id6svcurso
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_sala(self):
        return self.__sala
    
    def set_sala(self, sala):
        self.__sala = sala
        
    def get_valor(self):
        return self.__valor
    
    def set_valor(self, valor):
        self.__valor = valor
        
    def get_docente(self):
        return self.__docente
    
    def set_docente(self, docente):
        self.__docente = docente

    def get_tamano_sala(self):
        return self.__tamano_sala
    
    def set_tamano_sala(self, tamano_sala):
        self.__tamano_sala = tamano_sala
    
    def get_seccion(self):
        return self.__seccion
    
    def set_seccion(self, seccion):
        self.__seccion = seccion
    
    def get_duracion(self):
        return self.__duracion
    
    def set_duracion(self, duracion):
        self.__duracion = duracion
    
    def get_disponibilidad(self):
        return self.__disponibilidad
    
    def set_disponibilidad(self, disponibilidad):
        self.__disponibilidad = disponibilidad

    def __str__(self):
        cadena = '------\n'
        cadena += f'Nombre: {self.__nombre}\n'
        cadena += f'Sala: {self.__sala}\n'
        cadena += f'Valor: {self.__valor}\n'
        cadena += f'Docente: {self.__docente}\n'
        cadena += f'Tamaño de Sala: {self.__tamano_sala}\n'
        cadena += f'Sección: {self.__seccion}\n'
        cadena += f'Duración: {self.__duracion}\n'
        cadena += f'Disponibilidad: {self.__disponibilidad}\n'
        return cadena
