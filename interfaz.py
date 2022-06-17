from administrador_datos import *
from juego import *
from jugador import *
from consulta import *

print()
print("***********************************************************")
print("*¡¡¡Bienvenido a los Los 8 Escalones de la Programación!!!*")
print("***********************************************************")

opcion = ""
while opcion != "salir":
    print()
    opcion = input("Elilja el modo que desea: \n 1. Modo Carga de datos\n 2. Jugar\n 3. Consultas\n salir\n")

    match opcion:
        case "1":
            cargar_pregunta()
        case "2":
            crear_jugador()
            jugar()
        case "3":
            ranking()
        case _:
            pass