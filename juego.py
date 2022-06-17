import json
from random import randint
from administrador_datos import cargar_datos
from  jugador import *

def jugar():
    print()
    print("Escalon N°", jugador["escalon"], "!!!!!")
    print(jugador["nombre"], "Puntaje:", jugador["puntaje"])
    pregunta = nueva_pregunta()
    print(pregunta["pregunta"])

    mostrar_opciones(pregunta)

    respuesta = input()

    if respuesta.lower() == pregunta["correcta"].lower():
        print("Es correcto")
        sumar_puntaje()
        subir_escalon()
        jugar()
    else:
        print("Es Incorrecto")
        if jugador["escalon"] != 8:
            jugar()
        else:
            fin_juego()
            cargar_datos()
            

def nueva_pregunta():
    with open('preguntas.json', 'rt', encoding="utf-8") as list_pregutas:
        lista_preguntas = json.load(list_pregutas)
    return lista_preguntas[randint(0,len(lista_preguntas) - 1)]

def mostrar_opciones(pregunta):
    for i in pregunta["opciones"]:
        print(i)

def fin_juego():
    print("Fin del juego")
    jugador["nombre"]
    jugador["puntaje"]
    jugador["puntaje"]