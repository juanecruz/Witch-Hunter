import pygame,sys,manejo_imagenes

pygame.init()
w = 1200
h = 800

def main():
    #Se crea una fuente par complementar el titulo del juego
    miFuente = pygame.font.SysFont("Pixels",150)
    miTexto = miFuente.render("YOU WIN!",True,(200,200,200))
    #Se crea la ventana
    screen = pygame.display.set_mode((w,h))
    #Importacion y ejecucion de la musica
    musica = pygame.mixer.Sound("Audio/musica_inicio.mp3")
    musica.play(-1)
    #Ciclo principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((25,25,25))

        screen.blit(miTexto,(w/3,h/3))


        pygame.display.flip()
