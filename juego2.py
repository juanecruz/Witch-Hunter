import pygame, random

from Clases import *

def main():
    pygame.init()
    win = False
    ancho, alto = 1440, 720 #dimensiones de la pantalla
    
    rgb = 0 #color del tablero
    color_fondo = (rgb, rgb, rgb)
    
    margen_i = ancho/4 #dimensiones del tablero
    margen_f = 3*margen_i
    
    cuadro = (ancho/2)/6 #espacios para ubicar los troncos
    
    #sonidos
    sonido = pygame.mixer.music.load ("Audio/Bosque Misterioso.mp3")
    pygame.mixer.music.set_volume(0.25)
    sonido_madera = pygame.mixer.Sound ("Audio/Madera.mp3")
    sonido_ganar = pygame.mixer.Sound ("Audio/Ganar.mp3")
    
    #fondo de la pantalla
    fondo = pygame.image.load ("assets/fondo_juego2.png")
    fondo = pygame.transform.scale(fondo, (ancho, alto))
    
    pantalla = pygame.display.set_mode ((ancho, alto)) #carga pantalla
    clock = pygame.time.Clock()#carga un reloj que controla la cantidad de bucles
    
    #carga de imagenes de troncos necesarios
    imagen_tronco_a = pygame.image.load ("assets/tronco_a.png").convert()
    imagen_tronco_b = pygame.image.load ("assets/tronco_b.png").convert()
    imagen_tronco_x = pygame.image.load ("assets/tronco_x.png").convert ()
    
    #pone los troncos a jugar
    tronco_0 = Tronco ((margen_i + 2*cuadro, 4*cuadro), imagen_tronco_a)
    tronco_1 = Tronco ((margen_i + 0*cuadro, 3*cuadro), imagen_tronco_a)
    tronco_2 = Tronco ((margen_i + 3*cuadro, 0*cuadro), imagen_tronco_b)
    tronco_3 = Tronco ((margen_i + 2*cuadro, 5*cuadro), imagen_tronco_b)
    tronco_4 = Tronco_1 ((margen_i + 2*cuadro, 0*cuadro), imagen_tronco_a)
    tronco_5 = Tronco_1 ((margen_i + 5*cuadro, 1*cuadro), imagen_tronco_a)
    tronco_6 = Tronco_1 ((margen_i + 2*cuadro, 2*cuadro), imagen_tronco_a)
    tronco_7 = Tronco_1 ((margen_i + 4*cuadro, 3*cuadro), imagen_tronco_a)
    tronco_8 = Tronco_1 ((margen_i + 1*cuadro, 4*cuadro), imagen_tronco_a)
    tronco_9 = Tronco_1 ((margen_i + 5*cuadro, 3*cuadro), imagen_tronco_b)
    tronco_x = Tronco ((margen_i + 0*cuadro, 2*cuadro), imagen_tronco_x)
    
    #listas con todos los troncos
    all_sprite_list = pygame.sprite.Group()
    tronco0_sprite_list = pygame.sprite.Group()
    tronco1_sprite_list = pygame.sprite.Group()
    tronco_move_list = pygame.sprite.Group()
    
    #añade los troncos a las listas
    all_sprite_list.add (tronco_0, tronco_1, tronco_2, tronco_3, tronco_4, tronco_5, tronco_6, tronco_7, tronco_8, tronco_9, tronco_x) #lista de todos los sprites
    tronco0_sprite_list.add (tronco_0, tronco_1, tronco_2, tronco_3, tronco_x)#lista con los troncos horizontales
    tronco1_sprite_list.add (tronco_4, tronco_5, tronco_6, tronco_7, tronco_8, tronco_9)#lista con los troncos verticales
    
    jugando = True #me dice si estoy jugando o no
    mover_tronco = False
    while jugando: #bucle del juego
        #ZONA DE EVENTOS ___________________________________________________________________
        
        mouse_pos = pygame.mouse.get_pos()
        for evento in pygame.event.get ():
            if evento.type == pygame.QUIT:#si se debe quitar la pantalla cuando la cierro
                jugando = False
                
            if evento.type == pygame.MOUSEBUTTONDOWN: #doy click en el mouse para mover los troncos, y segun sea la posicion del mouse este lo va a trasladar
                for tronco in all_sprite_list:
                    if mouse_pos[0] > tronco.rect.x and mouse_pos[0] < tronco.rect.x + tronco.width and mouse_pos[1] > tronco.rect.y and mouse_pos[1] < tronco.rect.y + tronco.height:
                        mover_tronco = True
                        tronco_move_list.add (tronco)
                        
            if evento.type == pygame.MOUSEBUTTONUP: #si se levanta el botón del mouse entonces este deja de mover el tronco
                for tronco in tronco_move_list:
                    tronco_move_list.remove (tronco)
                mover_tronco = False
                
        #ZONA DE ANALISIS DE MOVIMIENTO_____________________________________________________
        if win == True:
            pygame.mixer.music.stop()
            import juego3

        if mover_tronco: #cuando se mueve el tronco
            for tronco in tronco_move_list: #para cada tronco que se esta moviendo
                if tronco in tronco0_sprite_list: #si el tronco se mueve horizontalmente este se mueve, y la pos. del mouse ayuda a mover el tronco
                    tronco.rect.x = mouse_pos[0] - tronco.width/2
                elif tronco in tronco1_sprite_list:
                    tronco.rect.y = mouse_pos[1] - tronco.height/2
                
                #hace que el tronco no sobrepase el tablero (el ancho)
                if tronco.rect.x < margen_i:
                    tronco.rect.x = margen_i
                elif tronco.rect.x + tronco.width > margen_f:
                    tronco.rect.x = margen_f - tronco.width
                
                #hace que el tronco no sobrepase el tablero (el alto)
                if tronco.rect.y < 0:
                    tronco.rect.y = 0
                elif tronco.rect.y + tronco.height > alto:
                    tronco.rect.y = alto - tronco.height
                    
            for tronco in tronco_move_list:
                all_sprite_list.remove(tronco) #aca elimina el tronco de todos los sprites, para que al momento de mirar la siguiente lista, este no se tome a si mismo
                for tronco0 in all_sprite_list: #aca revisa cada tronco que esta en pantalla
                    if tronco.rect.colliderect(tronco0.rect):#si el tronco colisiona con algun otro tronco
                        if tronco in tronco0_sprite_list and tronco0 in tronco1_sprite_list: #mira si el tronco que toco es uno horizontal:
                            #detiene al tronco si este va horizontalmente
                            if tronco.rect.x < tronco0.rect.x:
                                tronco.rect.x = tronco0.rect.x - tronco.width
                            elif tronco.rect.x > tronco0.rect.x:
                                tronco.rect.x = tronco0.rect.x + tronco0.width
                        if tronco in tronco1_sprite_list and tronco0 in tronco0_sprite_list: #mira si el tronco con el que choco es uno vertical:
                            #se detiene si va verticalmente
                            if tronco.rect.y < tronco0.rect.y:
                                tronco.rect.y = tronco0.rect.y - tronco.height
                            elif tronco.rect.y > tronco0.rect.y:
                                tronco.rect.y = tronco0.rect.y + tronco0.height
                        sonido_madera.play() #reproduce el sonido para identificar que los troncos se tocaron
                        mover_tronco = False #deja de mover el tronco
                all_sprite_list.add(tronco) #vuelve a añadir el tronco a todos los sprites para que lo dibuje despues
        
        #me identifica si el tronco rojo (el que debe salir) ya salio del tablero
        if tronco_x.rect.x + tronco_x.width <= margen_f and tronco_x.rect.x >= margen_i + 4*cuadro:
            tronco_x.rect.x = margen_f
            mover_tronco = False
            sonido_ganar.play()
            win = True
        
        #ZONA DE DIBUJO___________________________________________________________
        
        pantalla.blit (fondo, (0, 0))#dibuja el fondo de la pantalla
        s = pygame.image.load ("assets/instrucciones.png").convert() #agrega una imagen que dirá las instrucciones
        s.set_colorkey(blanco)#le quita el color blanco a la imagen de las instrucciones
        
        """
        Debido a que en pygame las imagenes que se cargan no vienen con el color alpha ya incorporado, por lo que es necesario crear
        una nueva superficie que sí admita dicho color.
        mientras que se aumenta el valor alpha, este máximo puede llegar hasta 512, por lo que se procede a "jugar" con ese valor
        de la siguiente manera:
        """
        if rgb < 512: #si es menor a 512 entonces que el programa siga aumentando la opacidad del color
            #aca es donde se carga las intrucciones
            s.set_alpha(rgb - 255)
            pantalla.blit (s, ((ancho/2)-180, 0))
            rgb += 8
        elif rgb == 512: #si llega a 512 entonces el programa se detiene por una cierta cantidad de tiempo
            pygame.time.delay(5000)
            s.fill (color_fondo)
            rgb += 1 #aca se le suma 1 al color alpha para que ya se quite la imagen de las intrucciones
            pygame.mixer.music.play()
        else:
            s = pygame.Surface((ancho/2, alto)) #se reemplaza la imagen de las instrucciones por la del tablero negro
            pantalla.blit (s, (margen_i, 0))
            fondo = pygame.image.load ("assets/fondo1_juego2.png").convert() #se coloca el fondo nuevamente, pero este fondo ya está editado con la flecha roja (flecha que se menciona en las intrucciones)
            all_sprite_list.update() #actualiza los sprites
            all_sprite_list.draw (pantalla)#dibuja todos los sprites
        
        pygame.display.flip () #refrezca la pantalla
        clock.tick(60)
    pygame.quit() #Quita Pygame
