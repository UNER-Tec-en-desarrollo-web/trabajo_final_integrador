from datetime import date

jugador = {
        "fecha" : "",
        "nombre": "",
        "puntaje": 0,
        "escalon": 1
    }

def crear_jugador():
    print()
    jugador ["fecha"] = str(date.today())
    jugador ["nombre"] = ""
    jugador ["nombre"] = input("Ingrese nombre: ")
    jugador ["puntaje"] = 0
    jugador ["escalon"] = 1
  
  
def sumar_puntaje():
    jugador["puntaje"] += 10

def subir_escalon():
    if jugador["escalon"] < 8:
        jugador["escalon"] += 1