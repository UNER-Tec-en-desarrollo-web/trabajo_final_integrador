from administrador_datos import *


def ranking():
    opcion = ""

    while opcion != "volver":
        print()
        opcion = input("Elija como desea filtrar las partidas\n 1. Por nombre\n 2. Por puntaje\n 3. Por fecha\n volver\n")

        match opcion:
            case "1":
                filtrar_nombre()
            case "2":
                filtrar_puntaje()
            case "3":
                filtrar_fecha()
            case _:
                pass