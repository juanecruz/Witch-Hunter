import pygame

blanco = [255, 255, 255]

"""
La clase Tronco es la clase que me va a definir la imagen, la altura y la anchura de los troncos, la creacion de los rectangulos por la imagen que se tome,
la posicion de dicho rectangulo, el ancho y el largo del rectangulo, y la actualizacion del rectangulo
"""

class Tronco (pygame.sprite.Sprite): #clase que hereda de los sprites de pygame
    def __init__ (self, position, img):#metodo constructor que toma como argumento la posicion del tronco y la imagen a tomar
        super().__init__()
        self.image = img
        self.image.set_colorkey (blanco)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect (position[0], position[1], self.width, self.height)
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect (self.rect.x, self.rect.y, self.width, self.height)

class Tronco_0 (Tronco): #clase del tipo Tronco que indica que son troncos horizontales
    def __init__ (self, position, img):
        super().__init__ (position, img)
        
class Tronco_1 (Tronco): #clase del tipo Tronco que indica que son troncos verticales
    def __init__ (self, position, img):
        super().__init__ (position, img)
        self.image = pygame.transform.rotate (self.image, 90)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect (self.rect.x, self.rect.y, self.width, self.height)
        
"""
En estas clases no hay metodos porque cada tronco depende de la posicion del mouse, la cual cambia a cada momento
"""