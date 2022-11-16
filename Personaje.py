import pygame,random
class Personaje(pygame.sprite.Sprite):
    direction = 0
    def __init__(self):
        super().__init__()
        self.frame = 0
        self.is_walking = False
        self.vel = 20
        self.image = animaciones[self.frame]
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height
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
            if self.rect.x > width:
                self.rect.x = 0
            elif self.rect.x < 0:
                self.rect.x = width
    def shoot(self):
        bala = Bala(self.rect.x+20,self.rect.y)
        musica_pelea.play()
        self.image = animaciones[13]
        all_sprite_group.add(bala)
        balas.add(bala)
