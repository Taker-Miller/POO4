import json
import requests
url = "https://larr.cl/larr.cl/json/prueba2023/generarRegistro.php"

nombre = input("Ingresa el nombre del curso: ").lower()
while True:
    try:
        sala = int(input("ingresa el numero de la sala: "))
        if sala > 0:
            break
        else:
            print("Debes ingresar un número mayor a 0")
    except:
        print("solo debes agregar valores numericos ")

while True:
    try:
        valor = int(input("Ingresa el valor del curso: "))
        if valor > 0:
            break
        else:
            print("Debes ingresar un número mayor a 0")
    except:
        print("Solo debes agregar valores numéricos.")

docente = input("Ingresa el nombre del docente: ").lower()

while True:
    try:
        tamano_sala = int(input("Ingresa el tamaño de la sala: "))
        if tamano_sala > 0:
            break
        else:
            print("Debes ingresar un número mayor a 0")
    except:
        print("solo debes agregar valores numericos ")

while True:
    try:
        seccion = int(input("Ingresa la sección: "))
        if seccion > 0:
            break
        else:
            print("Debes ingresar un número mayor a 0")
    except:
        print("solo debes agregar valores numericos ")

while True:
    try:
        duracion = int(input("Ingresa la duración: "))
        if duracion > 0:
            break
        else:
            print("Debes ingresar un número mayor a 0")
    except:
        print("solo debes agregar valores numericos ")

while True:
    disponibilidad = input("Ingresa la disponibilidad (disponible u ocupado): ").lower()
    if disponibilidad in ["disponible", "ocupado"]:
        break
    else:
        print("Debes ingresar 'disponible' u 'ocupado'.")

data = [ {"campo": "nombre", "valor": nombre},
        {"campo": "sala", "valor": sala},
        {"campo": "valor", "valor": valor},
        {"campo": "docente", "valor": docente},
        {"campo": "tamano_sala", "valor": tamano_sala},
        {"campo": "seccion", "valor": seccion},
        {"campo": "duracion", "valor": duracion},
        {"campo": "disponibilidad", "valor": disponibilidad}
        ]

d = {"tabla":"6svcurso","campos": data
}
y=json.dumps(d)
print(y)

di = {"json":"json",
      "datos": y
}

r=requests.post(url,di)
print(r)



