from tkinter import *
from tkinter import messagebox
import random
import time
import winsound
class Simon:
    def __init__(self):
        self.ventana = Tk()
        self.arreglo = ()
        self.marcador = 0
        self.mayor = 0
        self.contador = 0
        self.juegoI = False
        self.colores = ["amarillo", "azul", "rojo", "verde"]
        self.ventana.title("Simon")
        self.ventana.geometry("500x500")
        self.iniciarBotones()
        self.ventana.mainloop()
    def iniciarBotones (self):
        self.btnazul = Button(self.ventana, command=lambda : self.presionar("azul"), height=6, width=13, bg= "blue")
        self.btnazul.place(x=100,y=100)
        self.btnamarillo = Button(self.ventana, command=lambda: self.presionar("amarillo"), height=6, width=13, bg="yellow")
        self.btnamarillo.place(x=100, y=100)
        self.btnrojo = Button(self.ventana, command=lambda: self.presionar("rojo"), height=6, width=13, bg="red")
        self.btnrojo.place(x=100, y=100)
        self.btnverde = Button(self.ventana, command=lambda: self.presionar("verde"), height=6, width=13, bg="green")
        self.btnverde.place(x=100, y=100)
        self.btnIniciar = Button(self.ventana, command= self.iniciar, height=2, width=7,bg="white", text="Empezar")
        self.btnIniciar.place(x=175,y=40)
        self.etiqueta= Label(self.ventana, text= "Marcador : 0 Mayor : 0")
        self.etiqueta.place(x=40, y=30)
    def presionar(self):
        print("")
    def iniciar(self):
        self.contador= 0
        self.marcador= 0
        self.arreglo = []
        self.juegoI = True
        self.crearColor()
    def revisarTurno(self):
        if len(self.arreglo) == self.contador:
            self.contador = 0
            self.marcador += 1
            self.btnIniciar.after(1000,self.crearColor)

    def crearColor(self):
        print("")
    def cambio(self,btn, colorCambio, colorInicial, f, d):
        print("")
    def sonido(self,frecuencia,duarcion):
        winsound.Beep(frecuencia,duracion)
obj = Simon()



