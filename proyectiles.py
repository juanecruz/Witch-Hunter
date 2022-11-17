import pygame,manejo_imagenes,random

pygame.init()

class Laser(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Laser, self).__init__()
        self.image = pygame.image.load("assets/laser1.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Acid_ball(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Acid_ball, self).__init__()
        img = manejo_imagenes.resize_image(pygame.image.load("assets/Bola_acido.png"),3)
        self.image = img
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.speedy = 5
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > 800:
            self.kill()

class Gema(pygame.sprite.Sprite):
    def __init__(self,x,y):
        diamante = manejo_imagenes.resize_image(pygame.image.load("assets/Diamante.png"), 4)
        esmeralda = manejo_imagenes.resize_image(pygame.image.load("assets/Emerald.png"), 3)
        rubi = manejo_imagenes.resize_image(pygame.image.load("assets/Rubi.png"), 3.2)
        gemas = [diamante, rubi, esmeralda]
        super(Gema,self).__init__()
        self.image = gemas[random.randrange(0,3)]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
    def update(self):
        self.rect.y += 5
        if self.rect.top > 800:
            self.kill()
    def tipo(self):
        return self.image