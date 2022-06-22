import json
from jugador import *

def cargar_pregunta():
    consigna = input("Ingrese una pregunta: ")
    opciones = []

    for i in range(4):
        opciones.append(input("Ingrese una opcion: "))

    correcta = input("Indique cual es la opcion correcta: ")

    escalon = input("Indique del 1-8 en que escalon se usara la pregunta: ")

    while not escalon.isnumeric():
        escalon = input("Indique del 1-8 en que escalon se usara la pregunta: ")

        if escalon.isnumeric():
            if int(escalon) > 8 or int(escalon) < 1:
                escalon = ""
    
    pregunta = {
        "pregunta" : consigna,
        "opciones" : opciones,
        "correcta" : correcta,
        "escalon" : int(escalon)
    }

    with open('preguntas.json', 'rt', encoding="utf-8") as list_pregutas:
        lista_preguntas = json.load(list_pregutas)

    lista_preguntas.append(pregunta)

    with open('preguntas.json', 'wt', encoding="utf-8") as preguntas:
        json.dump(lista_preguntas, preguntas, indent=4)

def cargar_datos():

    partida = {
        "jugador" : jugador["nombre"],
        "fecha" : jugador["fecha"],
        "puntaje" : jugador["puntaje"]
    }

    with open('partidas.json', 'rt', encoding="utf-8") as list_partidas:
        lista_partidas = json.load(list_partidas)
    
    lista_partidas.append(partida)

    with open('partidas.json', 'wt', encoding="utf-8") as partidas:
        json.dump(lista_partidas, partidas, indent=4)



def extraer_datos():
    with open('partidas.json', 'rt', encoding= "utf-8") as partidas:
        lista_partidas = json.load(partidas) 
    return lista_partidas


def filtrar_nombre():
    lista = extraer_datos()
    lista_ordenada = sorted(lista, key=lambda x : x["jugador"].casefold())

    print()
    print("{:<10}".format("JUGADOR"), "{:<10}".format("PUNTAJE"), "{:<10}".format("FECHA"))
    for partida in lista_ordenada:
        print("{:<10}".format(partida["jugador"]), "{:<10}".format(partida["puntaje"]), "{:<10}".format(partida["fecha"]))


def filtrar_puntaje():
    lista = extraer_datos()
    lista_ordenada = sorted(lista, key=lambda x : x["puntaje"], reverse=True)

    print()
    print("{:<10}".format("JUGADOR"), "{:<10}".format("PUNTAJE"), "{:<10}".format("FECHA"))
    for partida in lista_ordenada:
        print("{:<10}".format(partida["jugador"]), "{:<10}".format(partida["puntaje"]), "{:<10}".format(partida["fecha"]))


def filtrar_fecha():
    lista = extraer_datos()
    lista_ordenada = sorted(lista, key=lambda x : x["fecha"], reverse=True)

    print()
    print("{:<10}".format("JUGADOR"), "{:<10}".format("PUNTAJE"), "{:<10}".format("FECHA"))
    for partida in lista_ordenada:
        print("{:<10}".format(partida["jugador"]), "{:<10}".format(partida["puntaje"]), "{:<10}".format(partida["fecha"]))

