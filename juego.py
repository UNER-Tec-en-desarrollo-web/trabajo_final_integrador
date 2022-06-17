import json
from random import randint
from administrador_datos import cargar_datos
from  jugador import *

def jugar():
    pregunta = nueva_pregunta()

    if jugador["escalon"] != 8:
        print()
        print("Escalon N°", jugador["escalon"], "!!!!!")
        print(jugador["nombre"], "Puntaje:", jugador["puntaje"])
    
        if es_correcta(pregunta): # hace la pregunta y verifica y se contesta correctamente
            print("Es correcto")
            sumar_puntaje()
            subir_escalon()
            jugar()
        else:
            print("Es Incorrecto")
            subir_escalon()           
            jugar()
    else:
        escalon_8(pregunta)
            

def nueva_pregunta():
    with open('preguntas.json', 'rt', encoding="utf-8") as list_pregutas:
        lista_preguntas = json.load(list_pregutas)
    return lista_preguntas[randint(0,len(lista_preguntas) - 1)]

def mostrar_opciones(pregunta):
    num_opcion = 1
    for i in pregunta["opciones"]:
        print(num_opcion, i)
        num_opcion += 1

def fin_juego():
    print("Fin del juego\n")
    
    print("FELICIDADES!!!\nOBTUVISTE PUNTAJE PERFECTO:", jugador["puntaje"]) if jugador["puntaje"] == 110 else print("Puntaje final:", jugador["puntaje"])
    

def es_correcta(pregunta):
    print(pregunta["pregunta"])
    mostrar_opciones(pregunta)
    respuesta = int(input())
    while respuesta < 1 or respuesta > 4:
        print("Opción incorrecta!!!")
        print()
        print(pregunta["pregunta"])
        mostrar_opciones(pregunta)
        respuesta = int(input())

    return pregunta["correcta"] == pregunta["opciones"][respuesta - 1]

def escalon_8(pregunta):
    contador = 0

    while contador < 4:
        print()
        print("Escalon N°", jugador["escalon"], " Final Boss!!!!!")
        print(jugador["nombre"], "Puntaje:", jugador["puntaje"])
        print("Contesta 4 preguntas para ganarle!!!")
        print(f"{contador}/4")
        pregunta = nueva_pregunta()
        if es_correcta(pregunta): # hace la pregunta y verifica y se contesta correctamente
            contador += 1   
            print("Es correcto")
            sumar_puntaje()
        else:
            print("Es Incorrecto")      
            contador = 5

    fin_juego()
    cargar_datos()