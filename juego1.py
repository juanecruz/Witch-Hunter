import random

import pygame,sys,personajes,random,proyectiles,manejo_imagenes,juego2

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
    font = pygame.font.Font("Fonts/Pixels.ttf",tamano)
    text_surface = font.render(texto,True,(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface,text_rect)
"""Crea un sistema de gemas aleatorio"""
def sis_gemas():
    diamante = manejo_imagenes.resize_image(pygame.image.load("assets/Diamante.png"),4)
    esmeralda = manejo_imagenes.resize_image(pygame.image.load("assets/Emerald.png"),3)
    rubi = manejo_imagenes.resize_image(pygame.image.load("assets/Rubi.png"),3.2)
    gemas = [diamante,rubi,esmeralda]
    random_gem = []
    for i in range(4):
        elemento = random.randrange(0,3)
        random_gem.append(gemas[elemento])
    return random_gem

def main():
    # Tamaño de la ventana
    width = 1200
    height = 800
    # Grupos de sprites
    all_sprite_group = pygame.sprite.Group()
    murcielagos = pygame.sprite.Group()
    laser = pygame.sprite.Group()
    acid = pygame.sprite.Group()
    gemas = pygame.sprite.Group()

    # Personaje
    p1 = personajes.Personaje(width, height, all_sprite_group, laser)
    # Puntaje y horda
    score = 0
    horda = 1
    # Se crean los primeros enemigos
    for i in range(horda):
        enemigo = personajes.Murcielago(acid, all_sprite_group)
        all_sprite_group.add(enemigo)
        murcielagos.add(enemigo)
    # Se añade el personaje a la lista de todos los sprites
    all_sprite_group.add(p1)
    #
    pygame.init()
    pygame.mixer.init()

    screen_size = (1200, 800)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    #Tiempo desde la ultima actualizacion del juego
    last_update = pygame.time.get_ticks()
    #Puntaje
    score = 0

    #Creacion de las vidas
    vidas = crear_vidas(5)
    #Creación del primer sistema de gemas
    sis_gem = sis_gemas()
    #Contador de cuantos patrones de gemas ha recolectado el jugador
    contador_gemas_recolectadas = 1
    vida = manejo_imagenes.resize_image(pygame.image.load("assets/corazon.png"), 4)

    # Posicion de las vidas en pantalla
    pos_vidas_x = width - 100
    pos_vidas_y = height

    pos_gemas_x = width / 4
    pos_gemas_y = 0

    # Se carga el fondo y los diferentes efectos de sonido
    fondo = pygame.image.load("assets/fondo.png")
    musica = pygame.mixer.Sound("Audio/night-run-125181.mp3")
    recolectar_gema = pygame.mixer.Sound("Audio/Ataque3.wav")
    recoleccion_total = pygame.mixer.Sound("Audio/colector.wav")
    musica_pelea = pygame.mixer.Sound("Audio/laser5.ogg")
    dano = pygame.mixer.Sound("Audio/Daño.mp3")

    musica.set_volume(0.2)
    musica.play(-1)


    lose = False
    win = False
    perdio = False

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
        now = pygame.time.get_ticks()
        all_sprite_group.update()
        if win == True:
            musica.stop()
            juego2.main()
        hits = pygame.sprite.groupcollide(murcielagos,laser,True,True)
        for hit in hits:
            score += 50
            gema = proyectiles.Gema(hit.rect.centerx,hit.rect.y)
            all_sprite_group.add(gema)
            gemas.add(gema)

        hi = pygame.sprite.spritecollide(p1,gemas,True)
        if hi:
            for i in sis_gem:
                if hi[0].image.get_size() == i.get_size():
                    sis_gem.remove(i)
                else:
                    pass
            recolectar_gema.play()
        else:
            pass
        h = pygame.sprite.spritecollide(p1,acid,True)
        if h:
            dano.play()
            del vidas[0]
        else:
            pass
        if len(vidas) <= 0:
            lose = True
            musica.stop()
        else:
            pass

        #Zona de dibujo
        all_sprite_group.draw(screen)
        #Se imprime el puntaje en pantalla
        texto(f"Score: {str(score)}",screen,80,150,0)
        #Se imprime el numero de vidas en pantalla
        for i in vidas:
            pos_vidas_y += 60
            screen.blit(i,(pos_vidas_x,pos_vidas_y))
        pos_vidas_y = 200
        #Se imprime el sistema de gemas en pantalla
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
        #Se crean nuevos enemigos
        if len(murcielagos.sprites()) == 0:
            horda += 1
            for i in range(horda):
                enemigo = personajes.Murcielago(acid,all_sprite_group)
                all_sprite_group.add(enemigo)
                murcielagos.add(enemigo)
        if score >= 7000:
            win = True
        #Refrescar Pantalla
        pygame.display.flip()
        clock.tick(120)

