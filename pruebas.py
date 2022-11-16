import pygame,sys

w = 1200
h = 800
titulo = pygame.image.load("assets/Titulo.png")
start = pygame.image.load("assets/Start.png")
font = pygame.font.SysFont("Pixels",50)
screen = pygame.display.set_mode((w,h))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0,0,0))

    screen.blit(titulo,(400,0))
    font.render("Hunter",True,(255,255,255))
    screen.blit(start,(450,500))


    pygame.display.flip()
