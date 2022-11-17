import pygame
"""Crea una lista que contiene todos los frames para la animación recibe dos parametros
 - el numero de imagenes que se quiere cargar 
 - el factor de la imagen(S: para reducir el tamaño y N: para no hacer nada)
 - Carpeta donde se encuentran las animaciones
 -Nombre de los archivos(Este es un nombre en general)
 """
def crear_lista_animaciones(num_imagenes,factor,carpeta,nombre):
    frames = []
    sz = 0 #En esta variable le diremos a la función si queremos
    if factor.capitalize() == "S":
        sz = 1.5
    for i in range(1,num_imagenes + 1):
        img = pygame.image.load(f"{carpeta}/{nombre}_{i}.png")
        x,y = img.get_size()
        resize_image = pygame.transform.scale(img,(x/sz,y/sz))
        frames.append(resize_image)
    return frames

def resize_image(img,n):
    x, y = img.get_size()
    new_img = pygame.transform.scale(img,(x/n,y/n))
    return new_img