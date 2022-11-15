import random

import pygame,sys

class Character(pygame.sprite.Sprite):
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
class Bat(pygame.sprite.Sprite):
    import random
    def __init__(self):
        super().__init__()
        self.frame = 0
        self.vel = 2
        self.image = enemigos[self.frame]
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(100,width-100)
        self.rect.bottom = random.randrange(200,300)
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 1000
    def update(self):
        now = pygame.time.get_ticks()
        self.rect.x += self.vel
        if self.rect.x > width - 150 or self.rect.x < 0:
            self.vel *= -1
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.shoot()
    def shoot(self):
        acid_ball = Acid_ball(self.rect.x,self.rect.y)
        acid.add(acid_ball)
        all_sprite_group.add(acid_ball)

class Bala(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Bala, self).__init__()
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
        img = resize_image(pygame.image.load("assets/Bola_acido.png"))
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

def crear_vidas(n):
    vidas = []
    for i in range(n):
        img = pygame.image.load("assets/corazon.png")
        x, y = img.get_size()
        new_img = pygame.transform.scale(img, (x / 4, y / 4))
        vidas.append(new_img)
    return vidas
def draw_text(texto,surface,tamano,x,y):
    font = pygame.font.SysFont("Pixels",tamano)
    text_surface = font.render(texto,True,(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface,text_rect)
def resize_image(img):
    x, y = img.get_size()
    new_img = pygame.transform.scale(img,(x/3,y/3))
    return new_img

def crear_gema():
    gemas = []
    nombres_gema = ["Diamante","Emerald","Rubi"]
    for i in nombres_gema:
        gema = pygame.image.load(f"assets/{i}.png")
        gemas.append(gema)
    return gemas


"""Crea una lista que contiene todos los frames para la animación recibe dos parametros
 - el numero de imagenes que se quiere cargar 
 - el factor de la imagen(S: para reducir el tamaño y N: para no hacer nada)
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

width = 1200
height = 800

all_sprite_group = pygame.sprite.Group()
balas = pygame.sprite.Group()
enemies = pygame.sprite.Group()
acid = pygame.sprite.Group()

animaciones = crear_lista_animaciones(14,"S","Ciclo_Movimiento","C")
enemigos = crear_lista_animaciones(2,"S","Enemigo","Murcielago")
gemas = crear_gema()
ult_enemigo = enemies.sprites()
print(enemigos)

p1 = Character()
score = 0
horda = 1

for i in range(horda):
    e1 = Bat()
    all_sprite_group.add(e1)
    enemies.add(e1)

all_sprite_group.add(p1)
diamante = pygame.image.load("assets/Diamante.png")

pygame.init()
pygame.mixer.init()

screen_size = (1200,800)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
score = 0
vidas = crear_vidas(5)
pos_vidas_x = width - 100
pos_vidas_y = height

fondo = pygame.image.load("assets/fondo.png")
musica = pygame.mixer.Sound("Audio/night-run-125181.mp3")
musica_pelea = pygame.mixer.Sound("Audio/laser5.ogg")
dano = pygame.mixer.Sound("Audio/Daño.mp3")


musica.play()
lose = False


while not lose:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p1.shoot()
    #PINTAR PANTALLA
    screen.fill((13,10,15 ))
    screen.blit(fondo,[0,0,width,height])

    #LOGICA
    all_sprite_group.update()

    hits = pygame.sprite.groupcollide(enemies,balas,True,True)
    for hit in hits:
        score += 50
        crear_gema()
    h = pygame.sprite.spritecollide(p1,acid,True)
    if h:
        dano.play()
        del vidas[0]
    if len(vidas) <= 0:
        lose = True

    #ZONA DE DIBUJO
    all_sprite_group.draw(screen)
    draw_text(f"Score: {str(score)}",screen,80,150,0)
    for i in vidas:
        pos_vidas_y += 60
        screen.blit(i,(pos_vidas_x,pos_vidas_y))
    pos_vidas_y = 200
    if len(enemies.sprites()) == 0:
        horda += 1
        for i in range(horda):
            e1 = Bat()
            all_sprite_group.add(e1)
            enemies.add(e1)
    #Refrescar Pantalla
    pygame.display.flip()
    clock.tick(60)
