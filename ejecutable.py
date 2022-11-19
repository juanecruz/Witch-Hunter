import pygame,sys,manejo_imagenes,juego1

pygame.init()
w = 1200
h = 800

#Se carga el fondo de inicio
fondo_inicio = pygame.image.load("assets/fondo_inicio.png")
#Se carga la imagen con el titulo del juego
titulo = pygame.image.load("assets/Titulo.png")
titulo_rect = titulo.get_rect()
titulo_rect.centerx = w/2
#Se carga el boton de Start
start = manejo_imagenes.resize_image(pygame.image.load("assets/Start.png"),1.5)
start_rect = start.get_rect()
#Se crea una fuente par complementar el titulo del juego
miFuente = pygame.font.SysFont("Pixels",150)
miTexto = miFuente.render("HUNTER",True,(200,200,200))
#Se crea la ventana
screen = pygame.display.set_mode((w,h))
#Importacion y ejecucion de la musica
musica = pygame.mixer.Sound("Audio/musica_inicio.mp3")
musica.play(-1)
#Ciclo principal
while True:
    mouse = pygame.mouse.get_pos()
    mousex,mousey = mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and start_rect.width <= mousex and start_rect.height >= mousey:
            musica.stop()
            juego1.main()
        else:
            musica.play()




    screen.fill((25,25,25))

    screen.blit(fondo_inicio,(0,0))

    screen.blit(titulo,(20,-50))
    screen.blit(start,(1000,20))

    screen.blit(miTexto,(60,130))


    pygame.display.flip()
