import random

import pygame,sys

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
            if self.rect.x > width + 50:
                self.rect.x = 0
            elif self.rect.x < 0 - 100:
                self.rect.x = width
    def shoot(self):
        bala = Bala(self.rect.x+20,self.rect.y)
        musica_pelea.play()
        self.image = animaciones[13]
        all_sprite_group.add(bala)
        balas.add(bala)
class Murcielago(pygame.sprite.Sprite):
    import random
    def __init__(self):
        super().__init__()
        self.frame = 0
        self.vel = 2
        self.image = enemigos[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(100,width-100)
        self.rect.bottom = random.randrange(200,300)
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 1000
    def update(self):
        now = pygame.time.get_ticks()
        self.rect.x += self.vel
        if self.rect.x > width - 160 or self.rect.x < 0:
            self.vel *= -1

        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            self.image = enemigos[self.frame]

            if self.frame >= 1:
                self.frame = 0
            self.shoot()
    def shoot(self):
        acid_ball = Acid_ball(self.rect.x,self.rect.y)
        acid.add(acid_ball)
        all_sprite_group.add(acid_ball)
    def dejar_gema(self):
        gema = Gema(self.rect.centerx,self.rect.y)
        all_sprite_group.add(gema)

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
        img = resize_image(pygame.image.load("assets/Bola_acido.png"),3)
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
        diamante = resize_image(pygame.image.load("assets/Diamante.png"), 4)
        esmeralda = resize_image(pygame.image.load("assets/Emerald.png"), 3)
        rubi = resize_image(pygame.image.load("assets/Rubi.png"), 3.2)
        gemas = [diamante, rubi, esmeralda]
        super(Gema,self).__init__()
        self.image = gemas[random.randrange(0,3)]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
    def update(self):
        self.rect.y += 5
        if self.rect.top > height:
            self.kill()
    def tipo(self):
        return self.image



"""Crea una lista con n numero de vidas"""
def crear_vidas(n):
    vidas = []
    for i in range(n):
        img = pygame.image.load("assets/corazon.png")
        x, y = img.get_size()
        new_img = pygame.transform.scale(img, (x / 4, y / 4))
        vidas.append(new_img)
    return vidas

"""Crea un texto en pantalla
 - El texto que se quiere mostrar
 - La superficie o sea la ventana
 - tamaño
 - posición
 """
def texto(texto,surface,tamano,x,y):
    font = pygame.font.SysFont("Pixels",tamano)
    text_surface = font.render(texto,True,(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface,text_rect)

"""Reduce el tamaño de una imagen en un factor que se le de
 - imagen
 - factor 
 """
def resize_image(img,n):
    x, y = img.get_size()
    new_img = pygame.transform.scale(img,(x/n,y/n))
    return new_img
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

def sis_gemas():
    diamante = resize_image(pygame.image.load("assets/Diamante.png"),4)
    esmeralda = resize_image(pygame.image.load("assets/Emerald.png"),3)
    rubi = resize_image(pygame.image.load("assets/Rubi.png"),3.2)
    gemas = [diamante,rubi,esmeralda]
    random_gem = []
    for i in range(4):
        elemento = random.randrange(0,3)
        random_gem.append(gemas[elemento])
    return random_gem

#Tamaño de la ventana
width = 1200
height = 800
#Grupos de sprites
all_sprite_group = pygame.sprite.Group()
murcielagos = pygame.sprite.Group()
balas = pygame.sprite.Group()
acid = pygame.sprite.Group()
gemas = pygame.sprite.Group()

#Listas de animaciones
animaciones = crear_lista_animaciones(14,"S","Ciclo_Movimiento","C")
enemigos = crear_lista_animaciones(2,"S","Enemigo","Murcielago")
#Personaje
p1 = Personaje()
#Puntaje y horda
score = 0
horda = 1
#Se crean los primeros enemigos
for i in range(horda):
    enemigo = Murcielago()
    all_sprite_group.add(enemigo)
    murcielagos.add(enemigo)
#Se añade el personaje a la lista de todos los sprites
all_sprite_group.add(p1)
#
pygame.init()
pygame.mixer.init()

screen_size = (1200,800)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
last_update = pygame.time.get_ticks()
score = 0
vidas = crear_vidas(5)
sis_gem = sis_gemas()
contador_gemas_recolectadas = 1
vida = resize_image(pygame.image.load("assets/corazon.png"),4)


#Posicion de las vidas en pantalla
pos_vidas_x = width - 100
pos_vidas_y = height

pos_gemas_x = width / 4
pos_gemas_y = 0

#Se carga el fondo y los diferentes efectos de sonido
fondo = pygame.image.load("assets/fondo.png")
musica = pygame.mixer.Sound("Audio/night-run-125181.mp3")
recolectar_gema = pygame.mixer.Sound("Audio/Ataque3.wav")
recoleccion_total = pygame.mixer.Sound("Audio/colector.wav")
musica_pelea = pygame.mixer.Sound("Audio/laser5.ogg")
dano = pygame.mixer.Sound("Audio/Daño.mp3")

musica.set_volume(0.2)
musica.play(-1)


lose = False


while not lose:
    print(contador_gemas_recolectadas)
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
    now = pygame.time.get_ticks()
    all_sprite_group.update()

    hits = pygame.sprite.groupcollide(murcielagos,balas,True,True)
    for hit in hits:
        score += 50
        gema = Gema(hit.rect.centerx,hit.rect.y)
        all_sprite_group.add(gema)
        gemas.add(gema)

    hi = pygame.sprite.spritecollide(p1,gemas,True)
    if hi:
        for i in sis_gem:
            if hi[0].image.get_size() == i.get_size():
                sis_gem.remove(i)
        recolectar_gema.play()
    else:
        pass


    h = pygame.sprite.spritecollide(p1,acid,True)
    if h:
        dano.play()
        del vidas[0]
    if len(vidas) <= 0:
        lose = True

    #Zona de dibujo
    all_sprite_group.draw(screen)
    texto(f"Score: {str(score)}",screen,80,150,0)
    for i in vidas:
        pos_vidas_y += 60
        screen.blit(i,(pos_vidas_x,pos_vidas_y))
    pos_vidas_y = 200
    for i in sis_gem:
        pos_gemas_x += 100
        screen.blit(i,(pos_gemas_x,pos_gemas_y))
        if now - last_update >= 10000:
            sis_gem = sis_gemas()
            last_update = now
    pos_gemas_x = width/4
    if len(sis_gem) == 0:
        recoleccion_total.play()
        contador_gemas_recolectadas += 1
        score += 100
        sis_gem = sis_gemas()
    if contador_gemas_recolectadas % 5 == 0:
        contador_gemas_recolectadas = 1
        vidas.append(vida)
    if len(murcielagos.sprites()) == 0:
        horda += 1
        for i in range(horda):
            enemigo = Murcielago()
            all_sprite_group.add(enemigo)
            murcielagos.add(enemigo)

    #Refrescar Pantalla
    pygame.display.flip()
    clock.tick(120)
