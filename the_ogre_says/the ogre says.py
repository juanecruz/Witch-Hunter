from tkinter import * #tkinter es una vinculaculación 
from tkinter import messagebox
import random
import time
import winsound

class The_ogre_says: # con esto se va a empezar la clase para poder iniciar el juego, el juego será una especie de "Simón dice"
 def __init__(self):
  self.ventana=Tk() #con esto se crea la ventana
  self.arreglo=[]
  self.marcador=0 # la cantidad de puntos que llevamos en este juego 
  self.mayor=0 # puntuación maxima del juegador
  self.contador=0
  self.juegoI=False
  self.colores=["azul","amarillo","verde","rojo"] # las opciones de colores donde el jugador va a tocar para poder ganar el juego
  self.ventana.title("The_ogre_says")
  self.ventana.geometry("400x400")
  self.iniciar_B()
  self.ventana.mainloop()

 def iniciar_B(self):
  self.azul_b=Button(self.ventana,command=lambda: self.presionar("azul"),height=6,width=13,bg="blue")#con esto definimos el alto, el ancho y en que pocision se encuentra cada ventana (teniendo en cuenta el palno cortesiano)
  self.azul_b.place(x=100,y=100)

  self.amarillo_b=Button(self.ventana,command=lambda: self.presionar("amarillo"),height=6,width=13,bg="yellow")
  self.amarillo_b.place(x=200,y=100)

  self.rojo_b=Button(self.ventana,command=lambda: self.presionar("rojo"),height=6,width=13,bg="red")
  self.rojo_b.place(x=100,y=200)

  self.verde_b=Button(self.ventana,command=lambda: self.presionar("verde"),height=6,width=13,bg="green")
  self.verde_b.place(x=200,y=200)

  self.start_b=Button(self.ventana,command=self.iniciar, height=2,width=7,bg="white",text="Iniciar")
  self.start_b.place(x=175,y=40)

  self.etiqueta=Label(self.ventana,text="Marcador: 0 Mayor: 0")
  self.etiqueta.place(x=40,y=30)

 def presionar(self,color):# este constructor hace que cuando el jugador presione la opcion correcta, hace que incremente un punto en el marcador, asi hasta que pierda
    if self.juegoI==True:
        if len(self.arreglo) >= self.contador-1:
            if self.arreglo[self.contador]==color:
                self.contador+=1
                if color=="Amarillo":
                    self.sonido(600,500)# no todos los cuadors tienen el mismo sonido, asi que para diferenciarlo
                    if color=="Azul":
                        self.sonido(500,500)
                        if color=="Rojo":
                            self.sonido(700,500)
                            if color=="Verde":
                                self.sonido(800,500)
                                self.revisarTurno()

        self.etiqueta.config(text="Marcador: " + str(self.marcador) +"Mayor: " + str(self.mayor)) # cantidad de puntos que hemos hecho y el record nuestro

    else:

     messagebox.showinfo("Juego terminado","Has logrado hacer " + str(self.marcador) + "puntos.") # cuando fallemos al final del juego nos saldrá cuanto hemos hecho, (cuantos puntos)

     if self.marcador>self.mayor:
      self.mayor=self.marcador
     self.etiqueta.config(text="Marcador: " + str(self.marcador) +"Mayor: " + str(self.mayor))
     self.juegoI=False
     self.contador=0
     self.marcador=0
     self.arreglo=[]

 def iniciar(self):#con esta función se crea la funcion de empezar el juego
  self.contador=0
  self.marcador=0
  self.arreglo=[]
  self.juegoI=True
  self.crearColor()

 def revisarTurno(self):
  if len(self.arreglo)==self.contador:
   self.contador=0
   self.marcador+=1
   self.iniciar_B.after(1000,self.crearColor)
 def crearColor(self):
  if self.juegoI==True:
   i=0
   while i<len(self.arreglo):
    if self.arreglo[i]=="Azul":
     self.cambio(self.azul_b,"#6A5ACD","blue",500,500)#se crean el color de  cada uno de los cuadros( en este caso de amarillo, azul, rojo y verde )

    if self.arreglo[i]=="amarillo":
     self.cambio(self.amarillo_b,"#FFD700","yellow",600,500)

    if self.arreglo[i]=="rojo":
     self.cambio(self.rojo_b,"orange","red",700,500)

    if self.arreglo[i]=="verde":
     self.cambio(self.verde_b,"#00FF00","green",800,500)
    i+=1
    time.sleep(1)

   aleatorio=random.randrange(0,4)
   self.arreglo.append(self.colores[aleatorio])

   if self.arreglo[i]=="Azul":
     self.cambio(self.azul_b,"#6A5ACD","blue",500,500)# acá se define el color de los cuadros

   if self.arreglo[i]=="Amarillo":
     self.cambio(self.amarillo_b,"#FFD700","yellow",600,500)

   if self.arreglo[i]=="Rojo":
     self.cambio(self.rojo_b,"orange","red",700,500)

   if self.arreglo[i]=="Verde":
     self.cambio(self.verde_b,"#00FF00","green",800,500)


 def cambio(self,boton,colorCambio,ColorInicial,f,d):# acá se cambia el color 
  boton.config(bg=colorCambio)
  self.ventana.update()
  self.sonido(f,d)
  boton.config(bg=ColorInicial)
  self.ventana.update()

 def sonido(self,frecuencia,duracion):
  winsound.Beep(frecuencia,duracion)
  print("")

obj=The_ogre_says()
