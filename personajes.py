import pygame,manejo_imagenes,proyectiles,random,items

pygame.init()
pygame.mixer.init()

musica_pelea = pygame.mixer.Sound("Audio/laser5.ogg")
dano = pygame.mixer.Sound("Audio/Daño.mp3")

enemigos = manejo_imagenes.crear_lista_animaciones(2,"S","Enemigo","Murcielago")
animaciones = manejo_imagenes.crear_lista_animaciones(14,"S","Ciclo_Movimiento","C")

class Personaje(pygame.sprite.Sprite):
    direction = 0
    def __init__(self,widht,height,all_sprite_group,laser_group):
        super().__init__()
        self.all_sprite_group = all_sprite_group
        self.laser_group = laser_group
        self.width = widht
        self.height = height
        self.frame = 0
        self.is_walking = False
        self.vel = 20
        self.image = animaciones[self.frame]
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width / 2
        self.rect.bottom = self.height
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        cambio = 0
        if keys[pygame.K_RIGHT]:
            self.direccion = 1
            self.vel = 25
            cambio = 4
        elif keys[pygame.K_LEFT]:
            self.direccion = 2
            self.vel = -25
            cambio = 8
        else:
            self.direccion = 0

        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1

            if self.direccion != 0:
                self.image = animaciones[self.frame + cambio]
                self.rect.centerx += self.vel
                if self.frame >= 3:
                    self.frame = 0
            else:
                self.image = animaciones[self.frame]
                if self.frame >= 3:
                    self.frame = 0
            if self.rect.x > self.width:
                self.rect.x = 0
            elif self.rect.x < 0:
                self.rect.x = self.width
    def shoot(self):
        bala = proyectiles.Laser(self.rect.x+20,self.rect.y)

        musica_pelea.play()
        self.image = animaciones[13]

        self.all_sprite_group.add(bala)
        self.laser_group.add(bala)

class Murcielago(pygame.sprite.Sprite):
    import random
    def __init__(self,acid,all_sprite_group):
        super(Murcielago,self).__init__()
        self.all_sprite_group = all_sprite_group
        self.acid_group = acid
        self.frame = 0
        self.vel = 2
        self.image = enemigos[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(100,1200-100)
        self.rect.bottom = random.randrange(200,300)
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 1000
    def update(self):
        now = pygame.time.get_ticks()
        self.rect.x += self.vel
        if self.rect.x > 1200 - 160 or self.rect.x < 0:
            self.vel *= -1

        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            self.image = enemigos[self.frame]

            if self.frame >= 1:
                self.frame = 0
            self.shoot()
    def shoot(self):
        acid_ball = proyectiles.Acid_ball(self.rect.x,self.rect.y)
        self.acid_group.add(acid_ball)
        self.all_sprite_group.add(acid_ball)

