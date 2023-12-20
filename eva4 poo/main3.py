from DAO import DAO
import requests
from Curso import Curso
url="https://larr.cl/larr.cl/json/prueba2023/6svcurso.json"
r=requests.get(url)
print(r)
data=r.json()
print(data)
def registrarCurso():
    for x in data:
        if x != None:
         c = Curso (x["nombre"],x["sala"],x["valor"],x["docente"],x["tamano_sala"],x["seccion"],x["duracion"], x["disponibilidad"], x["id6svcurso"])
         print(c)
         dao=DAO()
         dao.registrarCurso(c)
        else:
            print("error")
   
  

while True:
    print('1.Registrar curso')
    print('2.Salir ')
    respuesta=input("ingrese una opcion: ")
    if respuesta=='1':
        registrarCurso()
    elif respuesta=='2':
        print("adios")
        break
    else:
        print("valor no valido")