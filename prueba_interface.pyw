from cProfile import label
from tkinter import *
from juego import *

def abrir_jugar():
    raiz.state(newstate="withdraw")
    ventana_jugar = Toplevel(raiz)

    ventana_jugar.title("Los 8 escalones de la Programación")
    ventana_jugar.resizable(0,0)
    # ventana_jugar.geometry("450x600")
    ventana_jugar.iconbitmap("red_stairs.ico")
    ventana_jugar.config(
        bg="blue",
        bd=45, 
        relief="groove", 
        cursor="hand2"
    )

    miFrame = Frame(ventana_jugar,width=450,height=600)
    miFrame.pack()
    miFrame.config(
    bg="red",
    bd=35, 
    relief="groove", 
    cursor="pirate"
    )

    salirButton = Button(
        miFrame, 
        text="Bye Bye!", 
        fg="red", 
        font=("Comic Sans MS", 10),
        command=quit
    ).place(x=10,y=450)

raiz = Tk()

raiz.title("Los 8 escalones de la Programación")
raiz.resizable(0,0)
# raiz.geometry("450x600")
raiz.iconbitmap("red_stairs.ico")
raiz.config(
    bg="blue",
    bd=45, 
    relief="groove", 
    cursor="hand2"
)

miFrame = Frame(raiz,width=450,height=600)
miFrame.pack()
miFrame.config(
    bg="red",
    bd=35, 
    relief="groove", 
    cursor="pirate"
)

miLabel = Label(
    miFrame, 
    text="Bienvenidos a Los 8 escalones de la Programación!!!", 
    fg="red",
    font=("Comic Sans MS", 12)
).place(x=0)

jugarButton = Button(
    miFrame, 
    text="A jugar!", 
    fg="red", 
    font=("Comic Sans MS", 10),
    command=abrir_jugar
).place(x=10,y=100)

cargarButton = Button(
    miFrame, 
    text="Agrega nuevas preguntas!", 
    fg="red", 
    font=("Comic Sans MS", 10),
).place(x=10,y=200)

rankButton = Button(
    miFrame, 
    text="Ve el ranking de jugadores", 
    fg="red", 
    font=("Comic Sans MS", 10),
).place(x=10,y=300)

salirButton = Button(
    miFrame, 
    text="Bye Bye!", 
    fg="red", 
    font=("Comic Sans MS", 10),
    command=quit
).place(x=10,y=450)

raiz.mainloop()